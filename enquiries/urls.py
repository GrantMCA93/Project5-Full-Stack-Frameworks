from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from enquiries import views as enquiries



urlpatterns = [

   	path('send_enquire_message/<int:user_id>/<int:house_id>',
         enquiries.send_enquire_message, name="send_enquire_message"),

]