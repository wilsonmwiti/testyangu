from django.db import models
# from ckeditor.fields import models.TextField
from django.db.models.fields.files import ImageField

# -----------------------BASE------------------------------------------
class Base(models.Model):
    logo=models.ImageField(upload_to="website/base",verbose_name="Logo image cropped and without background")
    icon=models.ImageField(upload_to="website/base", verbose_name="Logo Icon")
    facebook=models.URLField(max_length=50,verbose_name="Facebook",blank=True)
    twitter=models.URLField(max_length=50,verbose_name="Twitter",blank=True)
    linkedin=models.URLField(max_length=50,verbose_name="LinkedIn",blank=True)
    youtube=models.URLField(max_length=50,verbose_name="Youtube",blank=True)
    phone_number=models.CharField(max_length=14,verbose_name="Phone number",blank=True)
    email=models.EmailField(max_length=254,verbose_name="Email",blank=True)
    footer_advert=models.ImageField(upload_to="website/base",verbose_name="Footer image advert bellow newsletter")

    class Meta:
        db_table=u"Elimusmart links and resources"
# ---------------------HOME---------------------------------------------
class HomeCarouselOne(models.Model):
    main_heading=models.CharField(max_length=50,blank=True,verbose_name="Main heading")
    main_content=models.CharField(max_length=50,blank=True,verbose_name="Main content")
    secondary_heading=models.CharField(max_length=50,blank=True,verbose_name="Secondary heading")
    secondary_content=models.CharField(max_length=50,blank=True,verbose_name="Secondary content")
    bg_image=models.ImageField(upload_to='website/home',blank=False,verbose_name="Background image")

    class Meta:
        db_table=u"First home page carousel"

 
class HomeCarouselTwo(models.Model):
    main_heading=models.CharField(max_length=50,blank=True,verbose_name="Main heading")
    main_content=models.CharField(max_length=50,blank=True,verbose_name="Main content")
    secondary_heading=models.CharField(max_length=50,blank=True,verbose_name="Secondary heading")
    secondary_content=models.CharField(max_length=50,blank=True,verbose_name="Secondary content")
    bg_image=models.ImageField(upload_to='website/home',blank=False,verbose_name="Background image")

    class Meta:
        db_table=u"Second Home page carousel one"

 
class HomeAbout(models.Model):
    primary_title=models.CharField(blank=True, max_length=50,verbose_name="Title")
    primary_content=models.TextField(verbose_name="Content")
    mission=models.TextField(verbose_name="Our mission")
    first_image=models.ImageField(upload_to="website/home",verbose_name="Image size 370 by 348")
    second_image=models.ImageField(upload_to="website/home",verbose_name="Image size 370 by 471")
    
    class Meta:
        db_table=u"Home about us"

class BusinessSection(models.Model):
    heading=models.CharField(max_length=50,verbose_name="Heading")
    content=models.TextField(verbose_name="Content")
    first_point=models.CharField(max_length=50,verbose_name="Second point")
    second_point=models.CharField(max_length=50,verbose_name="First point",blank=True)
    image=models.ImageField( upload_to="website/home",verbose_name="Image")
    
    class Meta:
        db_table=u"Business section"
# 
class FAQImage(models.Model):
    image=models.ImageField(upload_to="website/home",verbose_name="image")
    
    class Meta:
        db_table=u"FAQ image"

class FAQ(models.Model):
    title=models.CharField(max_length=70,verbose_name="Title")
    content=models.TextField(verbose_name="Content")

    class Meta:
        db_table=u"FAQ "

class OurAdvantage(models.Model):
    title=models.CharField( max_length=50,verbose_name="Title")   
    content=models.TextField(verbose_name="Content")
    icon=models.CharField(max_length=50,verbose_name="Icon(please use favicon)",blank=True)
    
    class Meta:
        db_table=u"Our Insurance advantage"


class Quote(models.Model):
    title=models.CharField(max_length=70,verbose_name="Title")
    content=models.CharField(max_length=70,verbose_name="Content")
    phone=models.CharField(max_length=12,verbose_name="Phone")
    
    class Meta:
        db_table=u"Get a quote "

class ClientsFeedbacks(models.Model):
    photo=models.ImageField(upload_to="website/home/clients",verbose_name="Client's profile picture 80 by 80")
    content=models.TextField(verbose_name="What they say about elimusmart")
    name=models.CharField(max_length=50,verbose_name="Name")
    job_description=models.CharField(max_length=70,blank=True,verbose_name="Job description")

    class Meta:
        db_table=u"Testimonials"

        # -------------------------About-------------------------------------

class MainAbout(models.Model):
    header_bg=models.ImageField(upload_to="website/about",verbose_name="Header background")
    image=models.ImageField(upload_to="website/about",verbose_name="Image 550 by 542")
    main_heading=models.CharField(max_length=50,verbose_name="Main heading")
    content=models.TextField(verbose_name="Content")
    action_point_one=models.CharField(max_length=50,verbose_name="Action point one")
    action_point_two=models.CharField(max_length=50,verbose_name="Action point two")
    action_point_three=models.CharField(max_length=50,verbose_name="Action point three")
    action_point_four=models.CharField(max_length=50,verbose_name="Action point four")

    class Meta:
        db_table=u"Main about us"

class WhatWeDo(models.Model):
    image=models.ImageField(upload_to="website/about",verbose_name="Image")
    main_heading=models.CharField(max_length=50,verbose_name="Small one word Heading")
    small_heading=models.CharField(max_length=50,verbose_name="Big heading ")

    class Meta:
        db_table=u"What our cover entails"

        # -------------------------contact us----------------------------------
class ContactUsData(models.Model):
    bg_image=models.ImageField(upload_to="website/contact",)
    office_address=models.CharField(max_length=150,blank=True,verbose_name="Office address")
    primary_phone=models.CharField(max_length=50,verbose_name="Primary phone number")
    secondary_phone=models.CharField(max_length=50,blank=True,verbose_name="Secondary phone number")
    email=models.EmailField(max_length=254,verbose_name="Email")
    website=models.URLField(max_length=200,blank=True,verbose_name="Website")
    map_location=models.CharField(max_length=500,blank=True,verbose_name="Google map location")        

    class Meta:
        db_table=u"Contact us information"

class AccountsBackground(models.Model):
    login_bg_image=models.ImageField(upload_to="website/account",)
    sign_up_bg_image=models.ImageField(upload_to="website/account",)
    
    class Meta:
        db_table=u"Account login and sign-up backgrounds"