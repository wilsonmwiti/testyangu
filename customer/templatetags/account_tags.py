from authentication.accounts.models import Account
from customer.middleware import get_request
from django import template

import datetime

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