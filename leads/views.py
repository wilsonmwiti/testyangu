from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QuoteForm

from .models import QuoteLeads
from configuration.models import PremiumRate
from configuration.models import TaxRate

import string
import random

def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def sumassured(school_fees,number_of_years):
    sumassured=school_fees*number_of_years
    return sumassured

def premium(sum_assured):
    # sum assured*premium rate/100[1+Premium policy holder levy]
    rate=PremiumRate.objects.get(id='1')
    premium_rate=rate.rate
    per_one_thousands=sum_assured/1000
    new_rate=premium_rate/100
    premium=new_rate*sum_assured
    return premium

def tax(premium):
    rate=TaxRate.objects.get(id='1')
    tax_rate=rate.tax
    tax=premium*tax_rate
    return tax

def total(premium,tax):
    total=tax+premium
    return total

def leads(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        db =QuoteLeads()

        db.name = request.POST['names_as_they_appear_on_ID']
        db.email = request.POST['email']
        db.phone = request.POST['phone']
        db.dob = request.POST['dob']
        db.education_level = request.POST['school_level']
        annual_fees =request.POST['fees']
        school_years =request.POST['years']
        db.annual_fees=int(annual_fees)
        db.school_years=int(school_years)
        # calculating sum assured
        db.sum_assured=sumassured(db.annual_fees,db.school_years)
        # calculating premium
        db.premium=premium(db.sum_assured)
        db.tax=tax(db.premium)
        db.total=total(db.premium,db.tax)
        #generating order number
        db.order_number =id_generator()
        db.save()
        #saving value on sessions
        request.session['order_number']=db.order_number
        return HttpResponseRedirect("/checkout/")
    # if request.user.is_authenticated:
    #     first_name = request.user.first_name
    #     last_name = request.user.last_name
    #     email = request.user.email
    #     name=first_name+""+last_name
    #     form = ContactUsForm(request.POST,initial={'name':name,'email':email})
    # else:
    #     form=ContactUsForm()

    form=QuoteForm()
    return render(request,"leads/leads_form.html",{'form':form})