from django.contrib import admin


from .models import Order
from .models import Docs
from .models import KYC

admin.site.register(Order)
admin.site.register(Docs)
admin.site.register(KYC)