from django.urls import path
from . import views

urlpatterns = [
    path('donor/login/', views.donor_login),
    path('donor/dashboard/', views.donor_dashboard),
    path('patient/request/', views.blood_request),
    path('admin-request-history/', views.admin_requests),
    path('admin-blood/', views.blood_stock),
    path('home/', views.home),
]
