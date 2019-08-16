from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('password-reset/', views.login, name='password-reset'),

  
    
]
