from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicines.urls')),
    
    # Login configuration with template and redirects
    path('login/', 
         auth_views.LoginView.as_view(
             template_name='registration/login.html',
             redirect_authenticated_user=True  # Redirect logged-in users away from login page
         ), 
         name='login'),
         
    # Logout configuration with secure redirect
    path('logout/', 
         auth_views.LogoutView.as_view(
             next_page=reverse_lazy('login'),  # Redirect to login after logout
             template_name='registration/logged_out.html'  # Optional logout confirmation
         ), 
         name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)