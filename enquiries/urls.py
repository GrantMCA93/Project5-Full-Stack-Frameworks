from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from enquiries import views as enquiries



urlpatterns = [

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