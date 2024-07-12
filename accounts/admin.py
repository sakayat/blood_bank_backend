from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import DonorProfile

class DonorProfileAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'name', 'age', 'address', 'last_donation', 'available', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'name', 'age', 'address', 'last_donation', 'available')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(DonorProfile, DonorProfileAdmin)