from django.urls import path
from listings import views

urlpatterns = [
    path('', views.houses, name="houses"),
    path('house/addhouse/<int:user_id>', views.addhouse, name="addhouse"),
]