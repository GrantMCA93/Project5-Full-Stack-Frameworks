from django.urls import path
from listings import views as listings

urlpatterns = [
    path('', listings.houses, name="houses"),
        # listings folder 
    
    path('house/addhouse/<int:user_id>', listings.addhouse, name="addhouse"),
    path('', listings.houses, name="houses"),
    path('house/preview_house/<int:user_id>/<int:house_id>',
         listings.preview_house, name="preview_house"),
    path('house/pay_fee/<int:user_id>/<int:house_id>',
         listings.pay_fee, name="pay_fee"),
    path('house/<int:house_id>', listings.house, name="house"),

]