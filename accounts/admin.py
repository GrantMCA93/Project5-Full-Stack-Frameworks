from django.contrib import admin

from .models import UserProfile


class UserAdminFields(admin.ModelAdmin):
    list_display = ("user",  "phone", "terms", "joined")


admin.site.register(UserProfile, UserAdminFields)