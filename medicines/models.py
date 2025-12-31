# medicines/models.py
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.conf import settings

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255, blank=True)
    manufacturer = models.CharField(max_length=255)
    batch_number = models.CharField(max_length=100, unique=True)
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.batch_number})"

    def save(self, *args, **kwargs):
        # Important: This is the data format your scan view will parse
        qr_data = f"MED-{self.id}-{self.name}-{self.batch_number}"
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, 'PNG')
        buffer.seek(0)

        file_name = f'qr_{self.batch_number}.png'
        self.qr_code.save(file_name, File(buffer), save=False)
        
        super().save(*args, **kwargs)

class ScanLog(models.Model):
    scanned_data = models.TextField()
    recognized = models.BooleanField(default=False)
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        status = "Recognized" if self.recognized else "Unrecognized"
        return f"Scan by {self.user.username} - {status} - {self.timestamp}"