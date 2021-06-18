from django.urls import path

from .views import customer_mpesa_payment
from .views import mpesa_payment
from .views import stk_push_callback

urlpatterns = [
        path('pay-mpesa/',customer_mpesa_payment, name='mpesa'),
        path('mpesa/payment',mpesa_payment, name='mpesa_payment'),
        path('daraja/stk-push',stk_push_callback, name='mpesa_stk_push_callback'),
]