from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserAdminCreationForm, UserAdminForm

class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('email',)
        }),
        ('Informações Básicas', {
            'fields': ('first_name', 'last_login')
        }),
        ('Permissões', {
            'fields': ('active', 'is_staff', 'is_admin', 'is_superuser', 'groups', 'user_permissions')
        })
    )
    list_display = ['first_name', 'last_name', 'email', 'active', 'is_staff', 'is_admin', 'is_superuser', 'last_login']
    list_filter = ('active', 'is_staff')

admin.site.register(User, UserAdmin)