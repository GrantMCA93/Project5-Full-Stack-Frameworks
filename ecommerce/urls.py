"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from listings import urls as urls_listings
from enquiries import urls as urls_enquiries
from pages import urls as urls_pages
from listings import urls as urls_search
from accounts import urls_reset as urls_reset_accounts

from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    url('', include(urls_pages)),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^search/', include(urls_search)),
    url(r'^listings/', include(urls_listings)),
    url(r'^enquiries/', include(urls_enquiries)),
    url(r'^pages/', include(urls_pages)),
    url(r'^reset/', include(urls_reset_accounts)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
] 