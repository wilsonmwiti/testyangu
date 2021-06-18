from django.urls import path
from .views import claims

urlpatterns = [
        path('claims/',claims, name='claims'),
]