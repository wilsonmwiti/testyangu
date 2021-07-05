# ?dispenser
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.shortcuts import render
from .emails import send_mail
from django.urls import reverse


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

# ------------------------------------------------------------------------------------------------------------
# inactive email features
# generating pdf when kyc is approved
def send_kyc_information():
    kyc_id="Z34XXO2MN2H71OKR8LQUXJC0X"
    