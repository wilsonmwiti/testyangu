from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def claims(request):
    
    return render(request,"claims/claim_form.html")