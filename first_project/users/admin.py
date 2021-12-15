from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from todoapp.models import Project, ToDo
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'last_name', 'first_name', 'date_joined', 'is_staff', 'is_active',)
    list_filter = ('email', 'last_name', 'first_name', 'date_joined', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_name', 'first_name', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', \
                       'last_name', 'first_name', 'date_joined', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project)
admin.site.register(ToDo)
