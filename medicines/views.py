# medicines/views.py
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from .models import Medicine, ScanLog
from .forms import MedicineForm

# Optional: For Postgres Trigram search
try:
    from django.contrib.postgres.search import TrigramSimilarity
    POSTGRES_AVAILABLE = True
except ImportError:
    POSTGRES_AVAILABLE = False


@login_required
def medicine_list(request):
    query = request.GET.get('q', '')
    medicines = Medicine.objects.all().order_by('-created_at')

    if query:
        scored_medicines = []
        for med in medicines:
            name_score = fuzz.token_sort_ratio(query.lower(), med.name.lower())
            batch_score = fuzz.token_sort_ratio(query.lower(), med.batch_number.lower())
            max_score = max(name_score, batch_score)
            
            if max_score > 60:
                scored_medicines.append((-max_score, med))

        scored_medicines.sort()
        medicines = [med for (score, med) in scored_medicines]

    return render(request, 'medicines/medicine_list.html', {
        'medicines': medicines,
        'query': query,
    })


@login_required
def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'medicines/medicine_detail.html', {'medicine': medicine})


@login_required
def medicine_create(request):
    initial_data = {}
    scanned_data = request.GET.get('data', '')

    # Pre-fill form if QR data is provided
    if scanned_data:
        parts = scanned_data.split('-')
        if len(parts) >= 4 and parts[0] == 'MED':
            initial_data['name'] = parts[2]
            initial_data['batch_number'] = parts[3]

    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save()
            messages.success(request, f"Medicine '{medicine.name}' created successfully!")
            return redirect('medicine_detail', pk=medicine.pk)
    else:
        form = MedicineForm(initial=initial_data)

    return render(request, 'medicines/medicine_form.html', {
        'form': form, 'title': 'Add New Medicine', 'scanned_data': scanned_data
    })


@login_required
def medicine_update(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            medicine = form.save()
            messages.success(request, f"Medicine '{medicine.name}' updated successfully!")
            return redirect('medicine_detail', pk=medicine.pk)
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'medicines/medicine_form.html', {
        'form': form, 'title': f'Update {medicine.name}'
    })


@login_required
def medicine_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        name = medicine.name
        medicine.delete()
        messages.success(request, f"Medicine '{name}' deleted successfully!")
        return redirect('medicine_list')
    return render(request, 'medicines/medicine_confirm_delete.html', {'medicine': medicine})


@login_required
def scan_medicine(request):
    if request.method == 'POST':
        qr_data = request.POST.get('qr_data', '').strip()
        medicine = None
        error_message = None
        suggestions = []

        scan_log = ScanLog(user=request.user, scanned_data=qr_data)

        if not qr_data:
            error_message = "No data was scanned or entered. Please try again."
        else:
            # --- Recognition Logic ---
            try:
                parts = qr_data.split('-')
                if len(parts) >= 2 and parts[0] == 'MED':
                    medicine_id = int(parts[1])
                    medicine = Medicine.objects.get(pk=medicine_id)
            except (IndexError, ValueError, Medicine.DoesNotExist):
                # Fallback to batch number exact match
                try:
                    medicine = Medicine.objects.get(batch_number=qr_data)
                except Medicine.DoesNotExist:
                    # Optional: fuzzy search using Postgres TrigramSimilarity
                    if POSTGRES_AVAILABLE:
                        fuzzy_matches = Medicine.objects.annotate(
                            similarity=TrigramSimilarity('batch_number', qr_data)
                        ).filter(similarity__gt=0.3).order_by('-similarity')

                        if fuzzy_matches.exists():
                            scan_log.recognized = False
                            scan_log.save()
                            return render(request, 'medicines/scan_results.html', {
                                'matches': fuzzy_matches,
                                'search_term': qr_data,
                            })

        # --- Post-Recognition Actions ---
        if medicine:
            scan_log.recognized = True
            scan_log.medicine = medicine
            scan_log.save()
            return redirect('medicine_detail', pk=medicine.pk)
        else:
            scan_log.recognized = False
            scan_log.save()
            error_message = f"Medicine not found for the scanned data: '{qr_data}'"
            suggestions.append("Check if the QR code is clear and undamaged.")
            suggestions.append("Verify if the medicine has been registered in the system.")
            create_url = f"{reverse('medicine_create')}?data={qr_data}"
            suggestions.append(f"If this is a new medicine, you can <a href='{create_url}'>add it now</a>.")

        return render(request, 'medicines/scan_medicine.html', {
            'error': error_message,
            'suggestions': suggestions,
            'scanned_data': qr_data,
        })

    return render(request, 'medicines/scan_medicine.html')
