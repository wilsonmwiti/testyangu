from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

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
from .forms import ClaimsForm

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
        id_front=request.FILES['id_front']
        id_back=request.FILES['id_back']
        ira=request.FILES['ira']
        profile=request.FILES['profile']

        agent_code=agent_code_generator()
        url=str(get_current_site(request))+reverse("index")+"?q="+agent_code
        agent_identity=AgentIdentity(user=user,link=url,id_front=id_front,id_back=id_back,ira=ira,profile=profile)
        agent_identity.save()
        
        return redirect("customer_account")

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
    order_number=request.GET.get('q')
    order=Order.objects.get(order_number=order_number)
    # checking whether has previous uploaded national ID.
    try:
        userdocuments=Docs.objects.get(user=current_user)
    except Exception as e:
        userdocuments="none"
    if request.method=="POST":
        # saving documents
        if userdocuments=="none":
            id_front=request.FILES['id_front']
            id_back=request.FILES['id_back']
            document_id=document_id_generator()
            documents=Docs(
                user=current_user,
                doc_id=document_id,
                id_front=id_front,
                id_back=id_back,
            ) 
            documents.save()
            docs=Docs.objects.get(doc_id=document_id)
        else:
            docs=Docs.objects.get(user=current_user)

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
        source_of_income=request.POST['source_of_income']
        sum_assured=request.POST['sum_assured']
        public_office=request.POST.get('public_office',False)
        relative_public_office=request.POST.get('relative_public_office',False)
        us_citizen=request.POST.get('us_citizen',False)
        us_id=request.POST.get('us_id',"NA")
        # convert checkbox inputs to boolena
        if public_office == 'on':
            public_office = True
        else:
            public_office = False

        if relative_public_office== 'on':
            relative_public_office = True
        else:
            relative_public_office = False

        if us_citizen== 'on':
            us_citizen = True
        else:
            us_citizen = False    

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
            sum_assured=sum_assured,
            public_office=public_office,
            relative_public_office=relative_public_office,
            us_citizen=us_citizen,
            us_id=us_id,
            source_of_income=source_of_income,
            email=email,
            postal_code=postal_code,
            name_of_school=name_of_school,
            school_county=school_county,
            school_level=school_level,
            school_type=school_type,
            nominee_names=nominee_name,
            annual_fees=order.lead.annual_fees,
            years_of_schooling_covered=order.lead.school_years,
            nominee_relationship=nominee_relationship,
            nominee_dob=nominee_dob,
            nominee_phone=nominee_phone,
            docs=docs,
            status="Pending",
        )

        kyc.save()
        # saving beneficially manually
        # one
        beneficiary_names=request.POST['beneficiary_names']
        beneficiary_dob=request.POST['beneficiary_dob']
        beneficiary_allocation=request.POST['beneficiary_allocation']
        # two
        beneficiary=Beneficiary(
            kyc=kyc,
            beneficiary_names=beneficiary_names,
            beneficiary_dob=beneficiary_dob,
            beneficiary_allocation=beneficiary_allocation
        )
        beneficiary.save()
        # two
        if request.POST['beneficiary_names1']:
            beneficiary_names1=request.POST['beneficiary_names1']
            beneficiary_dob1=request.POST['beneficiary_dob1']
            beneficiary_allocation1=request.POST['beneficiary_allocation1']
            beneficiary1=Beneficiary(
                kyc=kyc,
                beneficiary_names=beneficiary_names1,
                beneficiary_dob=beneficiary_dob1,
                beneficiary_allocation=beneficiary_allocation1
            )
            beneficiary1.save()
        
            # Three
            if request.POST['beneficiary_names2']:
                beneficiary_names2=request.POST['beneficiary_names2']
                beneficiary_dob2=request.POST['beneficiary_dob2']
                beneficiary_allocation2=request.POST['beneficiary_allocation2']
                kyc=KYC.objects.get(kyc_id=kyc_id)
        
        
                beneficiary2=Beneficiary(
                    kyc=kyc,
                    beneficiary_names=beneficiary_names2,
                    beneficiary_dob=beneficiary_dob2,
                    beneficiary_allocation=beneficiary_allocation2
                )
                beneficiary2.save()

        # connecting order to kyc
        kyc_order=Order.objects.filter(order_number=order_number)
        kyc_order.update(kyc=kyc)
        return  redirect('/account/orders/')

    # rendering forms
    form=KYCForm()
    # info to be autofilled into the form
    name=order.lead.name
    dob=order.lead.dob
    sum_assured=order.lead.sum_assured
    phone=order.phone_number
    email=order.lead.email
    # autofilling kyc field
    form.fields['names'].initial =name
    form.fields['phone'].initial =phone
    form.fields['dob'].initial =dob
    form.fields['email'].initial = email
    form.fields['sum_assured'].initial = sum_assured
    docs=DocsForm()
    beneficiary=BeneficiaryForm()

    return render(request,'customer/kyc.html',{'form':form,
                                                'docs':docs,
                                                'order':order,
                                                'date':date,
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
    kyc=order.kyc
    if kyc.status=="Rejected":
        kyc_id=str(kyc.id)
        return redirect("kyc_edit",pk=kyc_id)

    beneficiaries=Beneficiary.objects.filter(kyc=kyc)
    return render(request,'customer/kyc_view.html',{'kyc':kyc,'beneficiaries':beneficiaries})


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

@login_required
def user_policy_list(request):
    user=request.user
    status="Active"
    policies=Order.objects.filter(owner=user,policy_status=status)
    return render(request,'customer/partials/user_policies_list.html',{'policies':policies})


@login_required
def expired_policy_list(request):
    user=request.user
    status="Expired"
    policies=Order.objects.filter(owner=user,policy_status=status)
    return render(request,'customer/partials/expired_policies_list.html',{'policies':policies})    
    
@login_required
def claims(request):
    form=ClaimsForm()
    return render(request,'customer/partials/claims.html',{'form':form})  
    