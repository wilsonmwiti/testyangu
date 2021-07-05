from functools import total_ordering
from random import choices
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from payments.mpesa.models import SuccessMpesaPayments
from django.contrib.auth.models import User
from leads.models  import  QuoteLeads
from configuration.models  import  Policy
from django.db import models
from customer.middleware import get_request

from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
import geonamescache

from communication.views import send_kyc_information
from communication.views import send_kyc_rejection_email

KENYAN_COUNTIES =(
    ("Baringo","Baringo"), 
    ("Bomet","Bomet"),   
    ("Bungoma","Bungoma"), 
    ("Busia","Busia"), 
    ("Elgeyo Marakwet","Elgeyo Marakwet"), 
    ("Embu","Embu"), 
    ("Garissa","Garissa"), 
    ("Homabay","Homabay"), 
    ("Isiolo","Isiolo"),
    ("Kajiado","Kajiado"), 
    ("Kakamega","Kakamega"), 
    ("Kericho","Kericho"), 
    ("Kiambu","Kiambu"), 
    ("Kilifi","Kilifi"), 
    ("Kirinyaga","Kirinyaga"), 
    ("Kisii","Kisii"), 
    ("Kisumu","Kisumu"), 
    ("Kitui","Kitui"), 
    ("Kwale","Kwale"), 
    ("Laikipia","Laikipia"), 
    ("Lamu","Lamu"),
    ("Machakos","Machakos"), 
    ("Makueni","Makueni"), 
    ("Mandera","Mandera"), 
    ("Marsabit","Marsabit"), 
    ("Meru","Meru"), 
    ("Migori","Migori"), 
    ("Mombasa","Mombasa"), 
    ("Murang'a","Murang`a"), 
    ("Nairobi","Nairobi"), 
    ("Nakuru","Nakuru"), 
    ("Nandi","Nandi"), 
    ("Narok","Narok"), 
    ("Nyamira","Nyamira"), 
    ("Nyandarua","Nyandarua"), 
    ("Nyeri","Nyeri"), 
    ("Samburu","Samburu"), 
    ("Siaya","Siaya"), 
    ("Taita Taveta","Taita Taveta"), 
    ("Tana River","Tana River"), 
    ("Trans Nzoia","Trans Nzoia"), 
    ("Tharaka Nithi","Tharaka Nithi"), 
    ("Turkana","Turkana"), 
    ("Uasin Gishu","Uasin Gishu"), 
    ("Vihiga","Vihiga"), 
    ("Wajir","Wajir"), 
    ("West Pokot","West Pokot"), 
)

STATUS_CHOICES = (
    ("Submit", "Submit KYC"),
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
)

MARITAL_STATUS_CHOICES=(
    ('Divorced','Divorced'),
    ('Married','Married'),
    ('Single','Single'),
)

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female')
)

TYPES_OF_SHOOL_CHOICES=(
    ('Private','Private'),
    ('Public','Public')
)

SCHOOL_LEVEL_CHOICES=(
    ('Primary','Primary'),
    ('Secondary','Secondary'),
    ('University/College','University/College')
)

POLICY_CHOICES=(
    ('Inactive','Inactive'),
    ('Active','Active'),
    ('Expired','Expired')
)

class Docs(models.Model):
    user=models.OneToOneField(User,verbose_name=("Owner"), on_delete=models.CASCADE)
    time=models.DateTimeField(verbose_name="Time added",auto_now_add=True)
    doc_id=models.CharField(max_length=50,verbose_name='Documents Number',default=0)
    id_front=models.FileField(upload_to='user/docs/nationalID/',verbose_name='ID Front')
    id_back=models.FileField(upload_to='user/docs/nationalID/',verbose_name='ID Back')
    verified=models.BooleanField(default=False,verbose_name="Verified")
    
    class Meta(object):
        db_table=u"ID Images"
    

class KYC(models.Model):
    time=models.DateTimeField(auto_now_add=True,verbose_name='Time')
    kyc_id=models.CharField(max_length=50,verbose_name='KYC Number')
    names=models.CharField(verbose_name="Applicant's Three Names as per ID",max_length=50)
    nationality=CountryField(verbose_name='Nationality')
    id_national=models.IntegerField(verbose_name='National ID/Passport NO')
    kra_pin=models.CharField(max_length=50,verbose_name='KRA PIN Number')
    gender=models.CharField(max_length=50,choices=GENDER_CHOICES,verbose_name='Gender')
    marital_status=models.CharField(max_length=50,choices=MARITAL_STATUS_CHOICES,verbose_name='Marital Status')
    occupation=models.CharField(max_length=50,verbose_name='Occupation')
    phone=models.IntegerField(verbose_name='Phone number')
    dob=models.CharField(max_length=50,verbose_name='Date of Birth')
    # benefits
    annual_fees=models.IntegerField(blank=True,verbose_name='Annual fees',default=0)
    years_of_schooling_covered=models.IntegerField(blank=True,default=0,verbose_name='Years of Schooling Covered')
    sum_assured=models.IntegerField(verbose_name='School Fees Insured')
    email=models.EmailField(max_length=254,verbose_name='Email Address')
    postal_code=models.CharField(max_length=50,verbose_name='Postal Code')
    name_of_school=models.CharField(max_length=50,verbose_name='Name of School')
    school_county=models.CharField(max_length=50 ,choices=KENYAN_COUNTIES,verbose_name="School County")
    school_type=models.CharField(max_length=50,choices=TYPES_OF_SHOOL_CHOICES,verbose_name="School Type")
    school_level=models.CharField(max_length=50,choices=SCHOOL_LEVEL_CHOICES,verbose_name="School Level")
    # us citizen
    us_citizen=models.BooleanField(default=False,verbose_name="A USA Citizen")
    us_id=models.CharField(max_length=50,blank=True,verbose_name="ID/Birth Cert No")
    # political
    public_office=models.BooleanField(default=False,verbose_name="Hold a public office?")
    relative_public_office=models.BooleanField(default=False,verbose_name="Relative holds a public office?")
    #
    source_of_income=models.CharField(max_length=50,verbose_name="Source of Premium")
    # nominee
    nominee_names=models.CharField(max_length=50,verbose_name="Nominee Name")
    nominee_relationship=models.CharField(max_length=50,verbose_name='Relationship with Parent')
    nominee_dob=models.CharField(max_length=50,verbose_name="Date of Birth")
    nominee_phone=models.IntegerField(verbose_name="Phone Number")
    docs=models.ForeignKey(Docs, verbose_name=("Documents"), on_delete=models.CASCADE)
    status=models.CharField(verbose_name='Status',max_length=20,choices=STATUS_CHOICES,default="Submit")
    reject_reason=models.CharField(verbose_name='Reason for Rejecting KYC',max_length=70,default="")
    approved_by=models.OneToOneField(User, verbose_name=("Approved by"), on_delete=models.CASCADE,blank=True,null=True,related_name="Approvedby")

    
    __original_status =None

    def __init__(self, *args, **kwargs):
        super(KYC, self).__init__(*args, **kwargs)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        user=get_request().user
        if self.status == "Approved":
            send_kyc_information(self.kyc_id)
        if self.status == "Rejected":
            send_kyc_rejection_email(self.kyc_id,self.reject_reason)
            pass
        super(KYC, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_status = self.status
        self.__original_approved_by =user
    class Meta(object):
        db_table=u"KYC"
    
class Beneficiary(models.Model):    
    kyc=models.ForeignKey(KYC,verbose_name=('KYC'), on_delete=models.CASCADE)
    beneficiary_names=models.CharField(max_length=50,verbose_name="Name")
    beneficiary_allocation=models.IntegerField(verbose_name="Allocation in  %",validators=[MaxValueValidator(100), MinValueValidator(1)])
    beneficiary_dob=models.CharField(max_length=50,verbose_name="Date of Birth")
   
    class Meta(object):
        db_table=u"Beneficiary"
    

class Order(models.Model):
    time=models.DateTimeField(auto_now_add=True,verbose_name="Time")
    order_number=models.CharField(max_length=50,verbose_name='Order Number')
    phone_number=models.CharField(max_length=50,verbose_name='Phone Number')
    category=models.CharField(max_length=70,default="Term Life Insurance",verbose_name="Category")
    package_name=models.CharField(max_length=70,default='Annual Premium',verbose_name="Package Category")
    product_name=models.CharField(max_length=70,default='Elimu Smart')
    payment=models.OneToOneField(SuccessMpesaPayments, verbose_name=("Payments"), on_delete=models.CASCADE,null=True,blank=True)
    owner=models.ForeignKey(User, verbose_name=("Owner"), on_delete=models.CASCADE)
    kyc=models.OneToOneField(KYC, verbose_name=("KYC"), on_delete=models.CASCADE,null=True,blank=True)
    features=models.OneToOneField(Policy, verbose_name=("Policy Feature"), on_delete=models.CASCADE,null=True,blank=True)
    lead=models.OneToOneField(QuoteLeads, verbose_name=("Lead"), on_delete=models.CASCADE)
    tax=models.IntegerField(verbose_name='Tax')
    premium=models.IntegerField(verbose_name='Premium')
    total=models.IntegerField(verbose_name='Total')
    status=models.CharField(verbose_name='Order Status',max_length=20,choices=STATUS_CHOICES,default="Pending")
    approved_by=models.OneToOneField(User, verbose_name=("Approved by"), on_delete=models.CASCADE,blank=True,null=True,related_name="approvedby")
    policy_number=models.CharField(max_length=50,blank=True,default="Please add")
    policy_status=models.CharField(max_length=50,blank=True,default="Inactive")

    class Meta(object):
        db_table=u"Order"
