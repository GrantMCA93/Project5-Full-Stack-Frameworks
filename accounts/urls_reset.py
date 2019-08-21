from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/', 
	   auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_change/done/', 
	   auth_views.PasswordChangeDoneView.as_view(),  name='password_change_done'),
    path('reset/<uidb64>/<token>/', 
	   auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',
	   auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', 
	   auth_views.PasswordChangeDoneView.as_view(),  name='password_change_done'),
]




