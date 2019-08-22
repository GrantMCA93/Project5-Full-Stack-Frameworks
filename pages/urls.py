from django.urls import path

from pages import views as pages

urlpatterns = [
	path('', pages.index, name="index"),
	path('contact', pages.contact, name="contact"),
	path('contact_thank_you_message', pages.contact_thank_you_message, name="contact_thank_you_message"),

]