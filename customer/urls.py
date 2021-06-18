from django.urls import path
from .views import customer
from .views import add_kyc
from .views import view_kyc
from .views import orders
from .views import order_view
from .views import docs_view
from .views import KycUpdateView
urlpatterns = [
        path('account/profile/',customer, name='customer_account'),
        path('account/kyc/add/',add_kyc, name='kyc-add'),
        path('account/kyc/edit/<int:pk>/',KycUpdateView.as_view(), name='kyc-edit'),
        path('account/kyc/view/',view_kyc, name='kyc-view'),
        path('account/orders/',orders, name='orders'),
        path('account/order/view/',order_view, name='order-view'),
        path('account/documents/view/',docs_view, name='docs-view'),
]