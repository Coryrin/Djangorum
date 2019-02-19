from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'moderator', 'sign_up_date')

admin.site.register(UserProfile, UserProfileAdmin)
