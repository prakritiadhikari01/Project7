from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/',views.profile, name='profile'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('profilee/', views.profilee, name='profilee'),
]
