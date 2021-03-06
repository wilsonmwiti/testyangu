from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from order.models import Order
class AgentIdentity(models.Model):
    user=models.OneToOneField(User, verbose_name="Agent", on_delete=models.CASCADE)
    link=models.CharField(max_length=100,verbose_name="Link(Use for referral)")
    id_front=models.FileField(upload_to="user/agent/id",verbose_name="National ID Front")
    id_back=models.FileField(upload_to="user/agent/id",verbose_name="National ID Back")
    ira=models.FileField(upload_to="user/agent/ira",verbose_name="IRA Licence")
    profile=models.FileField(upload_to="user/agent/profile",verbose_name="Profile Image")
    class Meta(object):
        db_table=u"Agent Identity Information"

class AgentBankAccount(models.Model):
    user=models.OneToOneField(User, verbose_name="Agent", on_delete=models.CASCADE)
    mpesa=models.CharField(blank=True,max_length=50,verbose_name="Mpesa")
    bank_name=models.CharField(blank=True,max_length=50,verbose_name="Bank Name")
    bank_branch=models.CharField(blank=True,max_length=50,verbose_name="Bank Branch")
    account_number=models.CharField(blank=True,max_length=50,verbose_name="Bank Account Number")
    class Meta(object):
        db_table=u"Agent Bank Account Information"        

class AgentLeads(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    agent_code=models.CharField(max_length=150)
    session=models.CharField(max_length=150)
    user_agent=models.CharField(max_length=150)

class AgentRegisteredUser(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    agent_code=models.CharField(max_length=150)
    session=models.CharField(max_length=150)
    type=models.CharField(max_length=150,default="self")
    user_agent=models.CharField(max_length=150)
    user=models.OneToOneField(User, verbose_name="Agent", on_delete=models.CASCADE)
