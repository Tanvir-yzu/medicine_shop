# medicines/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),
    path('medicine/new/', views.medicine_create, name='medicine_create'),
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),
    path('medicine/<int:pk>/edit/', views.medicine_update, name='medicine_update'),
    path('medicine/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
    path('scan/', views.scan_medicine, name='scan_medicine'),
]