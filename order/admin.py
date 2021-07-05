from django.contrib import admin
from reversion.admin import VersionAdmin
from import_export.admin import ExportActionMixin


from .models import Order
from .models import Beneficiary
from .models import Docs
from .models import KYC

class KYCAdmin(ExportActionMixin,admin.ModelAdmin):
     
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
     
    def has_add_permission(self, request, obj=None):
        # Disable delete
        return False    

    list_display= ( 'time','kyc_id','names','id_national','kra_pin','phone','dob','annual_fees','years_of_schooling_covered','sum_assured','status','approved_by',)
    list_display_links = ( 'time','kyc_id','names','id_national','kra_pin','phone','dob','annual_fees','years_of_schooling_covered','sum_assured','status','approved_by',)
    list_filter = ("time","approved_by","status" )
    search_fields = ("names","email","phone","id_national" )
    odering=("-id")

admin.site.register(Order)
admin.site.register(Beneficiary)
admin.site.register(Docs)
admin.site.register(KYC,KYCAdmin)