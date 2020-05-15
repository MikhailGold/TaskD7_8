from django.contrib import admin

# Register your models here.
from common.models import UserProfile

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    pass
