from django.urls import path
from .views import index
from .views import about
from .views import contact

urlpatterns = [
        path('', index, name='index'),
        path('about/', about, name='about'),
        path('contact/', contact, name='contact'),
]