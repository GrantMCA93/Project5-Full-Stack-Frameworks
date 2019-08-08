from django.urls import path

from pages import views as pages

urlpatterns = [
	path('', pages.index, name="index")
]