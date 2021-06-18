from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from website.cms.models import HomeCarouselOne
from website.cms.models import HomeCarouselTwo
from website.cms.models import HomeAbout
from website.cms.models import BusinessSection
from website.cms.models import FAQ
from website.cms.models import FAQImage
from website.cms.models import OurAdvantage
from website.cms.models import Quote
from website.cms.models import ClientsFeedbacks
from website.cms.models import MainAbout
from website.cms.models import WhatWeDo
from website.blog.models import Post
from website.cms.models import ContactUsData

from leads.models import ContactUs

from .form import ContactUsForm

def index(request):
    carouselOne=HomeCarouselOne.objects.all()
    carouselTwo=HomeCarouselTwo.objects.all()
    about=HomeAbout.objects.all()
    business=BusinessSection.objects.all()
    advantage=OurAdvantage.objects.all()
    faq=FAQ.objects.all()
    quote=Quote.objects.all()
    faqimage=FAQImage.objects.all()
    feedback=ClientsFeedbacks.objects.all()

    return render(request,'website/index.html',{'carouselOne':carouselOne,
                                                  'carouselTwo':carouselTwo,
                                                  'about':about,
                                                  'business':business,
                                                  'advantage':advantage,
                                                  'faqimage':faqimage,
                                                  'faq':faq,
                                                  'quote':quote,
                                                  'feedback':feedback,
                                                
    })

def about(request):
    about=MainAbout.objects.all()
    services=WhatWeDo.objects.all()
    post=Post.objects.all()

    return render(request,'website/about.html',{  'about':about,
                                                  'services':services,
                                                  'posts':post,

    })

def contact(request):
    information=ContactUsData.objects.all()
    if request.method =='POST':
        form = ContactUsForm(request.POST)
        data =ContactUs()

        data.name = request.POST.get('name'),
        name = request.POST.get('name'),
        data.email = request.POST.get('email'),
        data.phone = request.POST.get('phone'),
        data.subject = request.POST.get('subject')[0],
        data.message = request.POST.get('message'),
        
        data.save()
        messages.success(request,'We will get in touch soon.Thank you')
        return HttpResponseRedirect("/contact/")
    form=ContactUsForm()
    # if request.user.is_authenticated:
    #     first_name = request.user.first_name
    #     last_name = request.user.last_name
    #     email = request.user.email
    #     name=first_name+""+last_name
    #     form = ContactUsForm(request.POST,initial={'name':name,'email':email})
    #     return render(request,'website/contact.html',{'information':information,'form':form})    
    return render(request,'website/contact.html',{'information':information,'form':form})    

