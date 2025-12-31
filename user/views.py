# user/views.py

from django.urls import reverse_lazy
from django.views.generic import TemplateView

from allauth.account.views import LoginView, SignupView, LogoutView



# Login
login = LoginView.as_view(
    template_name='user/login.html',
    success_url=reverse_lazy('medicine_list'),
)



# Logout - Correct way
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect here after logout

logout = CustomLogoutView.as_view()