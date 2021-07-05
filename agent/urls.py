from django.urls import path
from .views import agent_referred_users
from .views import agent_add_customer
from .views import agent_quote_Lead_create
from .views import agent_view_order
from .views import agent_make_order
from .views import agent_leads

urlpatterns = [
        path('account/agent/leads/',agent_leads, name='agent_leads'),
        path('account/agent/referred-users/',agent_referred_users, name='agent_referred_users'),
        path('account/agent/referred-users/sign-up/', agent_add_customer, name='agent_add_customer'),
        path('account/agent/referred-users/generate-quote/',agent_quote_Lead_create, name='agent_generate_customer_quote'),
        path('account/agent/referred-users/view_order/',agent_view_order, name='agent_view_order'),
        path('account/agent/referred-users/order/',agent_make_order, name='agent_make_order'),

]