from django.contrib import admin

from .models import AnnualSchoolFees
from .models import SchoolLevel
from .models import MaximumAmountAllowed
from .models import Benefits
from .models import PremiumRate
from .models import TaxRate

class AnnualFeesAdmin(admin.ModelAdmin):

    list_display = ('time','fees')

class SchoolLevelAdmin(admin.ModelAdmin):

    list_display = ('time','school_level')

class MaximumAmountAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=MaximumAmountAllowed.objects.all().count()
        if count == 0:
            return True
        return False    
    list_display = ('time','amount')

class BenefitsAdmin(admin.ModelAdmin):
    
    list_display = ('premium','benefit')


class PremiumRateAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=PremiumRate.objects.all().count()
        if count == 0:
            return True
        return False    
    list_display = ('time','rate')

class TaxAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=TaxRate.objects.all().count()
        if count == 0:
            return True
        return False    
    list_display = ('time','tax')
admin.site.register(AnnualSchoolFees,AnnualFeesAdmin)
admin.site.register(SchoolLevel,SchoolLevelAdmin)
admin.site.register(MaximumAmountAllowed,MaximumAmountAdmin)
admin.site.register(Benefits,BenefitsAdmin)
admin.site.register(PremiumRate,PremiumRateAdmin)
admin.site.register(TaxRate,TaxAdmin)