from django.contrib import admin

from .models import Listing

class ListingAdminFields(admin.ModelAdmin):
	list_display = ('title', 'is_published', 'postcode', 'paid_fee', 'price', 'bedrooms', 'seller' , 'list_date')
	list_display_links = ('title', 'seller')
	list_editable = ('is_published',)

admin.site.register(Listing, ListingAdminFields)