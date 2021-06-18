import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import AllMpesaTransactions,MpesaCalls,SuccessMpesaPayments
       
          
class Calls(admin.ModelAdmin):
    def has_add_permission(self,request):
        return False
    def has_delete_permission(self,request):
        return False
    list_display= ['created_at','updated_at','ip_address','caller','conversation_id','content',]
    readonly_fields=[ 'created_at','updated_at','ip_address','caller','conversation_id','content', ]
    list_display_links = ('ip_address','caller','conversation_id','content', )
    list_filter = ['created_at']
    search_fields = ['ip_address']
    ordering = ('-created_at',) 
    list_per_page = 100 
    
class AllTransactions(admin.ModelAdmin):
    def has_add_permission(self,request):
        return False
    def has_delete_permission(self,request):
        return False
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    actions = ["export_as_csv"]
    export_as_csv.short_description = "Export Selected"
    list_display= ['created_at','merchant_id','checkout_request_id','Result_code','Result_description']
    readonly_fields=[ 'created_at','updated_at', 'merchant_id','checkout_request_id','Result_code','Result_description' ]
    list_display_links = ( 'merchant_id','checkout_request_id','Result_code','Result_description' )
    list_filter = ['created_at','Result_code']
    ordering = ('-created_at',) 
    list_per_page = 100 

class SuccessfulTransactions(admin.ModelAdmin):
    def has_add_permission(self,request):
        return False
    def has_delete_permission(self,request):
        return False

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    actions = ["export_as_csv"]
    export_as_csv.short_description = "Export Selected"
# 
    list_display= ['SystemDate','merchant_id','checkout_request_id', 'Amount','Receipt','Balance','TransactionDate','PhoneNumber',]
    readonly_fields=['SystemDate','merchant_id','checkout_request_id','Result_code','Result_description', 'Amount','Receipt','Balance','TransactionDate','PhoneNumber', ]
    list_display_links = ( 'merchant_id', 'Amount','Receipt','Balance','TransactionDate','PhoneNumber', )
    list_filter = ['TransactionDate',]
    search_fields = ['PhoneNumber',]
    ordering = ('-TransactionDate',) 
    list_per_page = 100 
    

admin.site.register(MpesaCalls,Calls)
admin.site.register(AllMpesaTransactions,AllTransactions)
admin.site.register(SuccessMpesaPayments,SuccessfulTransactions)