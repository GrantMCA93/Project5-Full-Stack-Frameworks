from django.urls import path
from listings import views as listings

urlpatterns = [
    path('', listings.houses, name="houses"),
    path('house/addhouse/<int:user_id>', listings.addhouse, name="addhouse"),

]