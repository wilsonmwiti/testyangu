from django.db import models

from django.db import models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
# M-pesa Payment models
class MpesaCalls(BaseModel):
    ip_address = models.TextField(default="safaricom")
    caller = models.TextField(default="APP#1")
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call/dev'
        verbose_name_plural = 'Mpesa Calls/dev'

class AllMpesaTransactions(BaseModel):
    merchant_id = models.TextField(verbose_name="merchant id",blank=True)
    checkout_request_id = models.TextField(verbose_name="checkout request id",blank=True)
    Result_code = models.TextField(verbose_name="Result code",blank=True)
    Result_description = models.TextField(verbose_name="result description",blank=True)
    class Meta:
        verbose_name = 'All mpesa transaction'
        verbose_name_plural = 'All Mpesa transactions'
        
class SuccessMpesaPayments(models.Model):
    SystemDate=models.DateTimeField(auto_now_add=True,verbose_name="System date")
    merchant_id = models.TextField(verbose_name="merchant id",blank=True)
    checkout_request_id = models.TextField(verbose_name="checkout request id",blank=True)
    Result_code = models.TextField(verbose_name="Result code",blank=True)
    Result_description = models.TextField(verbose_name="result description",blank=True)
    Amount= models.TextField(blank=True)
    Receipt=  models.TextField(blank=True)
    Balance=  models.IntegerField(blank=True ,default=0)
    TransactionDate= models.TextField(blank=True,verbose_name="transaction date")
    PhoneNumber=  models.TextField(blank=True,verbose_name="phone number")
    class Meta:
            verbose_name = 'Successful Mpesa transactions'
            verbose_name_plural = 'Successful Mpesa transactions'       
            