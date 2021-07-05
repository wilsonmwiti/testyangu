from django.urls import path
from .views import customer
from .views import add_kyc
from .views import view_kyc
from .views import orders
from .views import order_view
from .views import docs_view
from .views import KycUpdateView
from .views import user_policy_list
from .views import expired_policy_list
from .views import claims

urlpatterns = [
        path('account/profile/',customer, name='customer_account'),
        path('account/kyc/add/',add_kyc, name='kyc-add'),
        path('account/kyc/edit/<int:pk>/',KycUpdateView.as_view(), name='kyc_edit'),
        path('account/kyc/view/',view_kyc, name='kyc-view'),
        path('account/orders/',orders, name='orders'),
        path('account/order/view/',order_view, name='order-view'),
        path('account/documents/view/',docs_view, name='docs-view'),
        path('account/policies/',user_policy_list, name='userpolicies_list'),
        path('account/expired-policies/',expired_policy_list, name='expired_policies_list'),
        path('account/claims/',claims, name='claims'),
]