from django import template
from website.cms.models import AccountsBackground

register = template.Library()

@register.simple_tag
def account_background():
    data=AccountsBackground.objects.all()
    return data