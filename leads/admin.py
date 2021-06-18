from django.contrib import admin
from .models import ContactUs
from .models import QuoteLeads
from import_export.admin import ExportActionMixin
from reversion.admin import VersionAdmin
class ContactUsAdmin(ExportActionMixin,admin.ModelAdmin):
     
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
     
    def has_add_permission(self, request, obj=None):
        # Disable delete
        return False    

    list_display = ('id','time','name', 'phone','email','subject','responded',)
    list_display_links = ('id','time','name', 'phone','email','subject',)
    readonly_fields = ['id','time','name', 'phone','email','subject','message',]
    list_filter = ("time",'served_by','responded','converted' )
    search_fields = ("name","email","phone" )
    exclude = ('seen','time_responded')
    odering=("-id")


class LeadsAdmin(ExportActionMixin,VersionAdmin):
     
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
     
    def has_add_permission(self, request, obj=None):
        # Disable delete
        return False    

    list_display = ( 'name','order_number','email','phone','annual_fees','premium',)
    list_display_links = ('name','email')
    readonly_fields = [ 'time','name','dob','email','phone','annual_fees','premium','education_level','school_years',]
    list_filter = ("time",'served_by','contacted','converted' )
    search_fields = ("name","email","phone" )
    odering=("-id")


admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(QuoteLeads,LeadsAdmin)



   