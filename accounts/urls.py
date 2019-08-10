from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('password-reset/', views.login, name='password-reset'),
    # listings folder 
    path('house/addhouse/<int:user_id>', views.addhouse, name="addhouse"),
    path('', views.houses, name="houses"),
    path('house/preview_house/<int:user_id>/<int:house_id>',
         views.preview_house, name="preview_house"),
    
]
