from django.urls import path
from .views import agent_referred_users
from .views import agent_add_customer
from .views import agent_quote_Lead_create
from .views import agent_make_order

urlpatterns = [
        path('account/agent/referred-users/',agent_referred_users, name='agent_referred_users'),
        path('account/agent/referred-users/sign-up/', agent_add_customer, name='agent_add_customer'),
        path('account/agent/referred-users/generate-quote/',agent_quote_Lead_create, name='agent_generate_customer_quote'),
        path('account/agent/referred-users/make_order/',agent_make_order, name='agent_make_order'),
        path('account/agent/referred-users/KYC/',agent_make_order, name='agent_user_kyc'),

]