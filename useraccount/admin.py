from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'emp_id', 'is_staff', 'is_superuser']


admin.site.register(CustomUser, CustomUserAdmin)
