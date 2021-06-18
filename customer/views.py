from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse

from order.models import Beneficiary
from order.models import KYC
from order.models import Order
from order.models import Docs
from agent.models import AgentBankAccount, AgentIdentity
from authentication.accounts.models import Account
from django.contrib.sites.models import Site

from .forms import KYCForm
from .forms import DocsForm
from .forms import BeneficiaryForm
from .forms import AgentIdentityForm

import string
import random
import datetime

date=datetime.date.today()

# random integer and string generators
def agent_code_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def kyc_id_generator(size=25, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def document_id_generator(size=25, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# checking if user is an agent and if they have filled in added required details


@login_required
def customer(request):
    user=request.user
    if request.method=="POST":
        id_front=request.POST['id_front']
        id_back=request.POST['id_back']
        ira=request.POST['ira']
        profile=request.POST['profile']
        agent_code=agent_code_generator()
        url='127.0.0.1:8000'+reverse("index")+"?/"+agent_code
        agent_identity=AgentIdentity(user=user,link=url,id_front=id_front,id_back=id_back,ira=ira,profile=profile)
        agent_identity.save()
        return HttpResponseRedirect(reverse("customer_account"))

    account=Account.objects.get(user=user)
    agent_data=AgentIdentity.objects.filter(user=user).exists()

    if agent_data==True:
        agent_data=AgentIdentity.objects.get(user=user)

    form=AgentIdentityForm()
    return render(request,'customer/customer.html',{'date':date,
                                                     'account':account,
                                                     'form':form,
                                                     'agent_data':agent_data,
        })

@login_required
def orders(request):
    user=request.user
    orders=Order.objects.filter(owner=user)
    return render(request,'customer/partials/orders.html',{
                                                'date':date,
                                                'orders':orders,
    })

@login_required
def add_kyc(request):
    current_user=request.user
    # checking whether has previous uploaded national ID.
    try:
        userdocuments=Docs.objects.get(user=current_user)
    except Exception as e:
        userdocuments="none"
    if request.method=="POST":
        # saving documents
        if userdocuments:
            docs=Docs.objects.get(user=current_user)
            
        else:
            id_front=request.POST['id_front']
            id_back=request.POST['id_back']
            document_id=document_id_generator()
            documents=Docs(
                user=current_user,
                doc_id=document_id,
                id_front=id_front,
                id_back=id_back,
            ) 
            documents.save()
            docs=Docs.objects.get(doc_id=document_id)

        # saving kyc
        names=request.POST['names']
        nationality=request.POST['nationality']
        id_national=request.POST['id_national']
        kra_pin=request.POST['kra_pin']
        gender=request.POST['gender']
        marital_status=request.POST['marital_status']
        dob=request.POST['dob']
        occupation=request.POST['occupation']
        phone=request.POST['phone']
        email=request.POST['email']
        postal_code=request.POST['postal_code']
        name_of_school=request.POST['name_of_school']
        school_county=request.POST['school_county']
        school_type=request.POST['school_type']
        school_level=request.POST['school_level']
        nominee_name=request.POST['nominee_names']
        nominee_relationship=request.POST['nominee_relationship']
        nominee_dob=request.POST['nominee_dob']
        nominee_phone=request.POST['nominee_phone']

        kyc_id=kyc_id_generator()

        kyc=KYC(
            kyc_id=kyc_id,
            names=names,
            nationality=nationality,
            id_national=id_national,
            kra_pin=kra_pin,
            gender=gender,
            marital_status=marital_status,
            occupation=occupation,
            phone=phone,
            dob=dob,
            sum_assured=1500,
            email=email,
            postal_code=postal_code,
            name_of_school=name_of_school,
            school_county=school_county,
            school_level=school_level,
            school_type=school_type,
            nominee_names=nominee_name,
            nominee_relationship=nominee_relationship,
            nominee_dob=nominee_dob,
            nominee_phone=nominee_phone,
            docs=docs,
            status="Pending",
        )

        kyc.save()
        # saving beneficially
        beneficiary_names=request.POST['beneficiary_names']
        beneficiary_dob=request.POST['beneficiary_dob']
        beneficiary_allocation=request.POST['beneficiary_allocation']

        kyc=KYC.objects.get(kyc_id=kyc_id)

        beneficiary=Beneficiary(
            kyc=kyc,
            beneficiary_names=beneficiary_names,
            beneficiary_dob=beneficiary_dob,
            beneficiary_allocation=beneficiary_allocation
        )
        beneficiary.save()
        # connecting order to kyc
        order_number=request.GET.get('q')
        Order.objects.filter(order_number=order_number).update(kyc=kyc)
        HttpResponseRedirect('account/profile/')

    # rendering forms
    form=KYCForm()
    docs=DocsForm()
    beneficiary=BeneficiaryForm()
    return render(request,'customer/kyc.html',{'form':form,
                                                'docs':docs,
                                                'beneficiary':beneficiary,
                                                'userdocument':userdocuments,
    })
 
@method_decorator(login_required, name='dispatch')
class KycUpdateView(UpdateView):
    model = KYC
    form_class=KYCForm
    template_name= 'customer/kyc_update_form.html'
    success_url = '/thanks/'

@login_required
def view_kyc(request):
    order_number=request.GET.get('q')
    order=Order.objects.get(order_number=order_number)
    kyc_status=order.kyc.status
    print(kyc_status)
    print("------------------------------------")
    if kyc_status == "Approved":
        return render(request,'customer/kyc_view.html')
    else:
        kyc_pk=str(order.kyc.id)
        return HttpResponseRedirect('/account/kyc/edit'+'/'+kyc_pk+'/')   


@login_required
def order_view(request):
    order_number=request.GET.get('q')
    order=Order.objects.get(order_number=order_number)
   
    return render(request,'customer/partials/order_view.html',{'order':order,'date':date,})

@login_required
def docs_view(request):
    user=request.user
    docs=Docs.objects.filter(user=user)
                                                
    return render(request,'customer/partials/doc_view.html',{'docs':docs,'date':date,})