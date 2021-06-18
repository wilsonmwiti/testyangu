from django.urls import path
from .views import leads

urlpatterns = [
        path('quote/',leads, name='lead'),
]