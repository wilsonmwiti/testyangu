from django.contrib import admin
from django.db.models.query_utils import Q
from .models import Base
from .models import HomeCarouselOne
from .models import HomeCarouselTwo
from .models import HomeAbout
from .models import BusinessSection
from .models import OurAdvantage
from .models import FAQImage
from .models import FAQ
from .models import Quote
from .models import ClientsFeedbacks
from .models import WhatWeDo
from .models import MainAbout
from .models import ContactUsData
from.models import AccountsBackground

class BaseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=Base.objects.all().count()
        if count == 0:
            return True
        return False
    list_display = ("logo", "icon","footer_advert","facebook",'twitter','linkedin','facebook')

class CarouselOneAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=HomeCarouselOne.objects.all().count()
        if count == 0:
            return True
        return False
    list_display = ("id","main_heading","secondary_heading")

class CarouselTwoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=HomeCarouselTwo.objects.all().count()
        if count == 0:
            return True
        return False
    list_display = ("id","main_heading","secondary_heading")


class HomeAboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=HomeAbout.objects.all().count()
        if count == 0:
            return True
        return False
    list_display = ("id","primary_title")

class BusinessSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=BusinessSection.objects.all().count()
        if count == 0:
            return True
        return False
    list_display = ("id","heading")

class FAQImageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=FAQImage.objects.all().count()
        if count == 0:
            return True
        return False
    list_display = ("id","image")

class OurAdvantageFAQAdmin(admin.ModelAdmin):
    list_display = ("id","title")

class QuoteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=Quote.objects.all().count()
        if count == 0:
            return True
        return False
    list_display = ("id","title")

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id","name",'job_description')

class WhatWeDoAdmin(admin.ModelAdmin):
    list_display = ("id",'small_heading')    

class MainAboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=MainAbout.objects.all().count()
        if count == 0:
            return True
        return False

    list_display = ("id",'main_heading')

class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=ContactUsData.objects.all().count()
        if count == 0:
            return True
        return False

    list_display = ("id",'primary_phone','email','website')    

class AccountBackgroundAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=AccountsBackground.objects.all().count()
        if count == 0:
            return True
        return False

    list_display = ("id",)    

admin.site.register(Base,BaseAdmin)
admin.site.register(HomeCarouselOne,CarouselOneAdmin)
admin.site.register(HomeCarouselTwo,CarouselTwoAdmin)
admin.site.register(HomeAbout,HomeAboutAdmin)
admin.site.register(BusinessSection,BusinessSectionAdmin)
admin.site.register(OurAdvantage,OurAdvantageFAQAdmin)
admin.site.register(FAQImage,FAQImageAdmin)
admin.site.register(FAQ,OurAdvantageFAQAdmin)
admin.site.register(Quote,QuoteAdmin)
admin.site.register(ClientsFeedbacks,FeedbackAdmin)
admin.site.register(WhatWeDo,WhatWeDoAdmin)
admin.site.register(MainAbout,MainAboutAdmin)
admin.site.register(ContactUsData,ContactAdmin)
admin.site.register(AccountsBackground,AccountBackgroundAdmin)
