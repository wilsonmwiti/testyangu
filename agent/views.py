from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.forms import ValidationError

from authentication.accounts.models import Account
from leads.models import QuoteLeads
from .forms import SignUpForm
from leads.forms import QuoteForm

from payments.mpesa.views import MpesaCalls
from payments.mpesa.views import stkpush

from leads.views import id_generator
from leads.views import sumassured
from leads.views import premium
from leads.views import tax
from leads.views import total

from order.models import Order 
# Create your views here.
def agent_referred_users(request):
    return render(request,"agent/referred_users.html")


def agent_add_customer(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone=request.POST['phone']
        # Check to see if any users already exist with this email.
        try:
            match = User.objects.get(email=email)
            raise ValidationError('This email address is already in use.')

        except User.DoesNotExist:
            # Unable to find a user,
            user=User(first_name=first_name,last_name=last_name,email=email,is_active=False)
            user.save()
            user=User.objects.get(email=email)
            account_db=Account(user=user,phone_number=phone)
            account_db.save()
            return redirect('agent_generate_customer_quote')

    form=SignUpForm()
    return render(request,'agent/client/add.html',{'form':form,})


def agent_quote_Lead_create(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        db =QuoteLeads()
        db.name = request.POST['name']
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
        return redirect("agent_make_order")
    form=QuoteForm()    
    return render(request,'agent/client/generate_quote.html',{'form':form})

def agent_make_order(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        lead_order_number = request.POST["order_number"]
        user_data=QuoteLeads.objects.get(order_number=lead_order_number)
        amount=user_data.total
        number=str(phone)[-8:]
        national_code="07"
        phone_number=str((national_code+number))
        billed_amount=int(amount)
        mpesacall=MpesaCalls(ip_address=phone_number,content=billed_amount,conversation_id=1)
        mpesacall.save()
        # making and order
        order_number=id_generator()
        current_user = request.user
        lead=QuoteLeads.objects.get(order_number=lead_order_number)
        
            # saving order
        order=Order(
                order_number=order_number,
                phone_number=phone_number,
                owner= current_user,
                lead=lead,
                tax=lead.tax,
                premium=lead.premium,
                total=lead.total,
        )
        order.save()
        try: 
            # stkpush(request,phone_number,billed_amount)
            return redirect('agent_user_kyc')
        except Exception as error:
            user_agent=request.META['HTTP_USER_AGENT']
            messages.error(request,"There was a problem in initiating your transaction .Our engineers are currently fixing it.Sorry for the inconvenience",extra_tags='danger',)
            return redirect('/')     #also sho waiting modal       

    return render(request,'agent/client/make_order.html',)
    