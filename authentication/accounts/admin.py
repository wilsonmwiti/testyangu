from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from hijack_admin.admin import HijackUserAdminMixin

from .models import Activation
from .models import Account

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class AccountInline(admin.StackedInline):
#     model = Account
#     can_delete = False
#     verbose_name_plural = 'Users'
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (AccountInline,)

# hijacking action
class UserAdmin(BaseUserAdmin, HijackUserAdminMixin):
    list_display = (
        'hijack_field',  # Hijack button
    )

# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin) 
class AccountAdmin(admin.ModelAdmin):
     
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
     
    # def has_add_permission(self, request, obj=None):
    #     # Disable delete
    #     return False    

    list_display = ('user','account_type','phone_number')
    list_display_links = ('user','phone_number')
    # readonly_fields = ['user','phone_number',]
    list_filter = ("account_type",)
    search_fields = ("user","phone_number" )
    odering=("-id")

# admin.site.register(Activation) 
admin.site.register(Account,AccountAdmin) 
