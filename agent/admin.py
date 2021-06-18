from django.contrib import admin

from .models import AgentIdentity
from .models import AgentBankAccount
from .models import  AgentLeads

admin.site.register(AgentIdentity)