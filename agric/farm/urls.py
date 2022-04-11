from re import template
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('details/', views.see_details, name="details"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='farm/password_reset.html'), 
    name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='farm/password_reset_sent.html'), 
    name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='farm/password_reset_form.html'), 
    name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='farm/password_reset_done'), 
    name="password_reset_complete"),
    
]