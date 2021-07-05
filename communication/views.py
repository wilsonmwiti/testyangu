# ?dispenser
from django.http.request import HttpRequest
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.shortcuts import render
from .emails import send_mail
from django.urls import reverse
from django.shortcuts import render
# 
from django.template.loader import render_to_string
from weasyprint import HTML
import os
import base64
from django.core.files import File  # you need this somewhere
import urllib.request 

from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
from sendgrid import SendGridAPIClient
import imghdr

from order import models #kyc,order,--This is due to cyclic import 

def register_email(email,name):
    ctx = {
    'name': name
        }
    subject="WELCOME ABOARD"
    message= get_template('communication/emails/create_account_mail.html').render(ctx)
    send_mail(email,subject,message)

def login_email(email,name,user_agent,time): 
    ctx = {
    'name': name,
    'user_agent': user_agent,
    'time': time
        }   
    subject="Login From A New Device"
    message= get_template('communication/emails/login_email.html').render(ctx)
    send_mail(email,subject,message)

def order_email(email,name,order_number): 
    ctx = {
        'name': name,
        'order_number': order_number,
        }      
    subject="You Have a New Order"
    message= get_template('communication/emails/order_notification.html').render(ctx)

    send_mail(email,subject,message)

def agent_order_agent_notification_email(email,name,order_number,client_name): 
    ctx = {
        'name': name,
        'order_number': order_number,
        'client_name': client_name,
        }      
    subject="Client's Order Received"
    message= get_template('communication/emails/agent_order_agent_notification.html').render(ctx)

    send_mail(email,subject,message)



def agent_order_customer_notification_email(email,name,order_number,agent_name): 
    ctx = {
        'name': name,
        'order_number': order_number,
        'agent_name': agent_name,
        }      
    subject="You Have a New Order"
    message= get_template('communication/emails/agent_order_client_notification.html').render(ctx)

    send_mail(email,subject,message)


def send_reset_password_email(request, email, token, uid):
    url=request.build_absolute_uri(reverse('accounts:restore_password_confirm', kwargs={'uidb64': uid, 'token': token})),
    ctx = {
        'email':email,
        'url': url,
        }      
    subject="Reset Your Password"
    message= get_template('communication/emails/reset_password.html').render(ctx)
    send_mail(email,subject,message)

def send_activation_email(request, email, code):
    url=request.build_absolute_uri(reverse('accounts:activate', kwargs={'code': code})),
    ctx = {
        'email':email,
        'url': url,
        }      
    subject="Account Activation"
    message= get_template('communication/emails/account_activation.html').render(ctx)
    send_mail(email,subject,message)


def send_kyc_rejection_email(kyc,reason): 
    kyc=models.KYC.objects.get(kyc_id=kyc)
    order=models.Order.objects.get(kyc=kyc)
    name=order.owner.get_full_name()
    email=order.owner.email
    order_number=order.order_number
    ctx = {
        'name': name,
        'reason': reason,
        'order_number': order_number,
        }      
    subject="Submitted KYC Has Been Rejected"
    message= get_template('communication/emails/rejected_kyc.html').render(ctx)

    send_mail(email,subject,message)


# ------------------------------------------------------------------------------------------------------------
def send_kyc_information(kyc):
    SENDGRID_API_KEY="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"
    # geting kyc info
    base_url="https://elimusmart.duckdns.org/"
    kyc=models.KYC.objects.get(kyc_id=kyc)
    beneficiaries=models.Beneficiary.objects.filter(kyc=kyc)
    # Rendering pdf
    html_string = render_to_string('communication/kyc/kyc_pdf.html',{
        'kyc':kyc,
        'beneficiaries':beneficiaries
    })
    html = HTML(string=html_string, base_url=base_url)
    result = html.write_pdf()

    owner=models.Order.objects.get(kyc=kyc).owner
    docs=models.Docs.objects.get(user=owner)
    to=owner.email
    name=owner.get_full_name()
    subject="Elimusmart Client Information"
    content='Attached is the approved KYC document for'  + name +  'from ElimuSmart, The document has been checked and reviewed by ElimuSmart and has been forwarded for further processing'
    message = Mail(
        from_email='gmakara@bismart.co.ke',
        to_emails=to,
        subject=subject,
        html_content=content)
        
    # id_front = urllib.request.urlretrieve(base_url+docs.id_front.url)
    # id_back = urllib.request.urlretrieve(base_url+docs.id_back.url)

    encoded_pdf = base64.b64encode(result).decode()
    attachedKYC = Attachment(
        FileContent(encoded_pdf),
        FileName(name+'.pdf'),
        FileType('application/pdf'),
        Disposition('attachment')
    )

    message.attachment = attachedKYC   
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        # login unsent emails


    