# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='account_logout'),
    path('profile/', views.profile_view, name='profile'),  # ➡️ ADĂUGAT: ruta pentru profil
]
