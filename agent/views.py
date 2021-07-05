from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.forms import ValidationError
from django_user_agents.utils import get_user_agent

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
from .models import AgentIdentity 
from .models import AgentLeads
# from .models import AgentAddedUserOrder
from .models import AgentRegisteredUser

from communication.views import agent_order_agent_notification_email,agent_order_customer_notification_email
# Create your views here.
def agent_referred_users(request):
    current_user=request.user
    # orders=AgentAddedUserOrder.objects.filter(agent=current_user)
    return render(request,"agent/referred_users.html",)

def agent_leads(request):
    user=request.user
    agent=AgentIdentity.objects.get(user=user)
    agent_affiliate_link=agent.link
    agent_code=agent_affiliate_link[-6:]
    lead=AgentLeads.objects.filter(agent_code=agent_code)
    return render(request,"agent/leads.html",{'leads':lead})

def agent_add_customer(request):
    form=SignUpForm()
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone=request.POST['phone']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email already registered please use another email')
        else:
            user=User(username=email,first_name=first_name,last_name=last_name,email=email,is_active=True)
            user.save()
            user=User.objects.get(email=email)
            account_db=Account(user=user,phone_number=phone)
            account_db.save()
            # setting session for the next page
            request.session['first_name']=first_name
            request.session['last_name']=last_name
            request.session['email']=email
            #   saving user as agent referall
            agent=request.user
            agent=AgentIdentity.objects.get(user=agent)
            agent_affiliate_link=agent.link
            agent_code=agent_affiliate_link[-6:]
            user_agent = get_user_agent(request)
            session=request.session
            agent_add_user=AgentRegisteredUser(type="agent",agent_code=agent_code,session=session,user_agent=user_agent,user=user)
            agent_add_user.save()
            return redirect('agent_generate_customer_quote')
  
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
        order_number=id_generator()
        db.order_number =order_number
        db.save()
        #saving value on sessions
        # sending_email("order",db.email.email,db.name)
        request.session['order_number']=db.order_number
        return redirect("agent_view_order")
    if 'first_name' in request.session:
        # picking session for the previous page
        first_name=request.session['first_name']
        last_name=request.session['last_name']
        email=request.session['email']
        phone=request.session['phone']

    else:
        return redirect('agent_generate_customer_quote')

    form=QuoteForm()    
    names=first_name+last_name
    form.fields['name'].initial =names
    form.fields['email'].initial =email
    form.fields['phone'].initial =phone

    return render(request,'agent/client/generate_quote.html',{'form':form})

def agent_view_order(request):
    if 'order_number' in request.session:
            order_number= request.session['order_number']
    else:
        return redirect('agent_generate_customer_quote')
    data=QuoteLeads.objects.filter(order_number=order_number)   

    return render(request,'agent/client/view_order.html',{"data":data})

def agent_make_order(request):
    if request.method == "POST":
        phone=request.session['phone']
        email=request.session['email']
        lead_order_number = request.POST["order_number"]
        user_data=QuoteLeads.objects.get(order_number=lead_order_number)
        amount=user_data.total
        number=str(phone)[-8:]
        national_code="07"
        phone_number=str((national_code+number))
        billed_amount=int(amount)
        # making and order
        order_number=id_generator()
        customer = User.objects.get(email=email)
        lead=QuoteLeads.objects.get(order_number=lead_order_number)
            # saving order
        order=Order(
                order_number=order_number,
                phone_number=phone_number,
                owner= customer,
                lead=lead,
                tax=lead.tax,
                premium=lead.premium,
                total=lead.total,
        )
        order.save()
        # associating order with agent
        saved_order=Order.objects.get(order_number=order_number)
        current_user=request.user
        # agent_order=AgentAddedUserOrder(agent=current_user,order=saved_order)
        # agent_order.save()
        agent=request.user
        # sending emails
        agent_order_agent_notification_email(agent.email,agent.first_name,order_number,customer.first_name) 
        agent_order_customer_notification_email(email,customer.first_name,order_number,agent.first_name)


    return redirect('agent_referred_users')
    