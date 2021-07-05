from django.db import models
from django.db.models.fields import BooleanField, CharField, TextField
from django.contrib.auth.models import User

CONVERTED_CHOICES = [
    ('No', 'NO'),
    ('Yes', 'Yes'),
    ('NA', 'Not applicabe'),
]

class ContactUs(models.Model):
    time=models.DateTimeField(auto_now_add=True,verbose_name="Time")
    name=models.CharField(max_length=50,verbose_name="Names")
    email=models.EmailField(max_length=254,verbose_name="Email")
    phone=models.CharField(max_length=50,verbose_name="Phone")
    subject=models.CharField(max_length=70,verbose_name="Subject")
    message=models.TextField(verbose_name="Message")
    seen=models.BooleanField(default=False)
    responded=BooleanField(default=False,verbose_name="Contacted")
    notes =models.TextField(blank=True,verbose_name="Notes")
    converted=models.CharField(max_length=50,choices=CONVERTED_CHOICES,default="NO",verbose_name="Converted?")
    served_by=models.CharField(blank=True,max_length=50)

    class Meta(object):
        db_table=u"Contact us"

class QuoteLeads(models.Model):
    time=models.DateTimeField(auto_now_add=True,verbose_name="Time")
    order_number=models.CharField(max_length=50,verbose_name="Order number")
    name=models.CharField(max_length=100,verbose_name="Names As They Appear On ID")
    dob=models.DateField(verbose_name="Parents DoB")        
    email=models.EmailField(max_length=254,verbose_name="Email")
    phone=models.CharField(max_length=15,verbose_name="Phone number")
    annual_fees=models.IntegerField(verbose_name="Annual school fees")
    premium=models.IntegerField(verbose_name="premium")
    tax=models.IntegerField(verbose_name="Tax",default=0)
    total=models.IntegerField(verbose_name="Total",default=0)
    education_level=models.CharField(max_length=70,verbose_name="Child.s Education level")
    school_years=models.IntegerField(verbose_name="No of school years")
    sum_assured=models.IntegerField(verbose_name="sum_assured",blank=True)
    contacted=models.BooleanField(default=False,verbose_name="Contacted")
    converted=models.BooleanField(default=False,verbose_name="Converted")
    served_by=models.CharField(blank=True,max_length=100)
    notes=models.TextField(blank=True)
    
    class Meta(object):
        db_table=u"Quote Leads"
    