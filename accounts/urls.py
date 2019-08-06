from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, listings, addhouse, profile, logout, login

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^listings/$', listings, name='listings'),
    url(r'^addhouse/$', addhouse, name='addhouse'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]
