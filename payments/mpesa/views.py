from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
import requests
from django.urls import reverse
from requests.auth import HTTPBasicAuth
import json
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from datetime import datetime, timedelta
from django.contrib import messages

from leads.models import QuoteLeads
from .models import AllMpesaTransactions
from .models import MpesaCalls
from .models import SuccessMpesaPayments
from order.models import Order
from leads.models import QuoteLeads

import string
import random
import time

from communication.views import order_email

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required
def customer_mpesa_payment(request):
    if request.method=="POST":
        order_number = request.POST['order_number']
        user_data=QuoteLeads.objects.filter(order_number=order_number)
        return render(request,"mpesa/preview_and_payment.html",{'order_details':user_data})

   
def stkpush(request,phone_number,billed_amount):
    cl = MpesaClient()
    phone_number=phone_number
    amount=billed_amount
    account_reference = 'Oder payment'
    transaction_desc = 'Oder payment for roselian cakes '
    callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response.text)

@csrf_exempt        
def stk_push_callback(request): 
        mpesa_body_callback =request.body.decode('utf-8')
        mpesa_body=json.loads(mpesa_body_callback)
        body=mpesa_body.get('Body')
        stkcallback=body.get('stkCallback')
        merchant_id=stkcallback.get('MerchantRequestID')
        checkout_request_id=stkcallback.get('CheckoutRequestID')
        resultcode=stkcallback.get('ResultCode')
        result_desc=stkcallback.get('ResultDesc')
        callbacks= AllMpesaTransactions(
            merchant_id = merchant_id,
            checkout_request_id = checkout_request_id,
            Result_code = resultcode,
            Result_description =  result_desc
                )
        callbacks.save()
        if resultcode==0:
            items =stkcallback.get("CallbackMetadata")
            stkcallback=items.get("Item")
            Amount= stkcallback[0]
            Receipt= stkcallback[1]
            Balance= stkcallback[2]
            TransactionDate=stkcallback[3]
            PhoneNumber= stkcallback[4]
            global receipt
            global trans_date
            global Phone_number
            global amount
            amount=int(Amount.get("Value"))
            receipt=Receipt.get("Value")
            latest_record=SuccessMpesaPayments.objects.latest('id')
            balance=int(latest_record.Balance)
            new_balance=amount+balance
            date_data = str(TransactionDate.get("Value"))
            trans_date = datetime(year=int(date_data[0:4]), month=int(date_data[4:6]), day=int(date_data[6:8]),hour=int(date_data[8:10]),minute=int(date_data[10:12]),second=int(date_data[12:14]))
            phone_number=PhoneNumber.get("Value")
            successfullpayments=SuccessMpesaPayments(
            merchant_id = merchant_id,
            checkout_request_id = checkout_request_id,
            Result_code = resultcode,
            Result_description = result_desc,
            Amount=amount,
            Receipt=receipt,
            Balance=new_balance,
            TransactionDate = trans_date,
            PhoneNumber=phone_number,
            )
            return HttpResponsePermanentRedirect('/checkout/payment-details/#makeoder')
        else:
            # send mpesa error to user
            messages.error(request,result_desc,extra_tags='danger')
            return redirect('/checkout/payment-details/')
               
def mpesa_payment(request):
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
        # send email
        order_email(current_user.email,current_user.first_name,order_number)
        #make payment
        try: 
            # stkpush(request,phone_number,billed_amount)
            time.sleep(15) 
            return redirect('/account/profile/')
        except Exception as error:
            user_agent=request.META['HTTP_USER_AGENT']
            messages.error(request,"There was a problem in initiating your transaction .Our engineers are currently fixing it.Sorry for the inconvenience",extra_tags='danger',)
            return redirect('/checkout/')     #also sho waiting modal       

    return HttpResponse()  