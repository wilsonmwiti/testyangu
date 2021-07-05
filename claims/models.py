from django.db import models
from order.models import Order

class Claims(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    policy=models.OneToOneField(Order, verbose_name=("Policy"), on_delete=models.CASCADE)
    category=models.CharField(default="Term Life Insurance",max_length=50,verbose_name="Category")
    product=models.CharField(default="Elimu Smart",max_length=50,verbose_name="Product")
    product_package=models.CharField(default="Annual Premium",max_length=50,verbose_name="Product Package")
    policy_number=models.CharField(max_length=50,verbose_name="Policy Number")
    claim_amount=models.IntegerField(verbose_name="Claim Amount(in kSH)")
    message=models.TextField(verbose_name="Claims Proposal Message")
    school_bank_account= models.CharField(max_length=50,verbose_name="School Bank account")
    school_bank_account_branch=models.CharField(max_length=50,verbose_name="School Bank Balance")
    document=models.FileField(upload_to="user/claims/docs",verbose_name="Upload Documents")

