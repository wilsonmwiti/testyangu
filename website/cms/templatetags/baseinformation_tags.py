from django import template
from website.cms.models import Base
from website.cms.models import PageDescription
from website.cms.models import ThirdPartyTags

register = template.Library()

@register.simple_tag
def base_info():
    data=Base.objects.all()
    return data

@register.simple_tag
def page_description():
    description=PageDescription.objects.all()
    return description

@register.simple_tag
def third_party_tags():
    tags=ThirdPartyTags.objects.all()
    return tags

