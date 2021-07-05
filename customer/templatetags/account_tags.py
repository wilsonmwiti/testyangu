from authentication.accounts.models import Account
from customer.middleware import get_request
from django import template

import datetime

from agent.models import AgentIdentity

register = template.Library()

@register.simple_tag
def get_account():
    user=get_request().user
    account=Account.objects.get(user=user)
    return account

@register.simple_tag
def date():
    date=datetime.date.today()
    return date
    
@register.simple_tag
def agent_information():
    user=get_request().user
    try:
        agent_info=AgentIdentity.objects.get(user=user)
        exist=True
    except Exception:
        exist = False
    return exist    