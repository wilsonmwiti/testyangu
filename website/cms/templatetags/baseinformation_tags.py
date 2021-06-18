from django import template
from website.cms.models import Base

register = template.Library()

@register.simple_tag
def base_info():
    data=Base.objects.all()
    return data