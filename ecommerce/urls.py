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
from django.urls import path, include
from django.contrib import admin
from accounts import urls as urls_accounts
from listings import urls as urls_listings
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('$', all_products, name='index'),
    path('accounts/', include(urls_accounts)),
    path('listings/', include(urls_listings)),
    path('products/', include(urls_products)),
    path('cart/', include(urls_cart)),
    path('checkout/', include(urls_checkout)),
    path('search/', include(urls_search)),
    path('media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
] 

