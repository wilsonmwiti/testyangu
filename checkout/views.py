from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect

from leads.models import QuoteLeads

def checkout(request):
    if 'order_number' in request.session:
        order_number= request.session['order_number']
        print(order_number)
    else:
        HttpResponseRedirect("quote/")
    data=QuoteLeads.objects.filter(order_number=order_number)    
    return render(request,'checkout/checkout.html',{'data':data})
