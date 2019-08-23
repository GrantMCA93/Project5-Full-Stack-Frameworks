from django.urls import path
from listings import views as listings
from enquiries import views as enquiries

urlpatterns = [
    path('', listings.houses, name="houses"),
    path('house/addhouse/<int:user_id>', listings.addhouse, name="addhouse"),
    path('house/preview_house/<int:user_id>/<int:house_id>', listings.preview_house, name="preview_house"),
    path('house/pay_fee/<int:user_id>/<int:house_id>', listings.pay_fee, name="pay_fee"),
    path('house/<int:house_id>', listings.house, name="house"),
    path('house/edit_house/<int:user_id>/<int:house_id>',
         listings.edit_house, name="edit_house"),
    path('search', listings.search, name="search"),
    path('house/delete_house/<int:user_id>/<int:house_id>',
         listings.delete_house, name="delete_house"),
    path('search_by_links/<str:key>', listings.search_by_links, name="search_by_links"),
    path('search_by_user/<int:user_id>', listings.search_by_user, name="search_by_user"),
    
    # messaging 
    
   	path('send_enquire/<int:user_id>/<int:house_id>',
         enquiries.send_enquire, name="send_enquire"),
     path('send_contact_message/',
         enquiries.send_contact_message, name="send_contact_message"),
   	path('get_messages/', enquiries.get_messages, name="get_messages"),
   	path('toggle_read/<int:user_id>/<int:conversation_member>/<int:house_id>',
   	     enquiries.toggle_read, name="toggle_read"),
   	path('delete_message/<int:user_id>/<int:conversation_member>/<int:house_id>',
         enquiries.delete_message, name="delete_message"),
]