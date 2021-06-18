from django.db import models
from django.contrib.auth.models import User

ACCOUNT_CHOICES=(
    ('User', "user"),
    ('Agent', "Agent"),
    ('Admin',"Admin"),
    ('Super_Admin', "Super Admin"),
    ('Developer', "Developer"),
)
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15 ,verbose_name="phone number",default="none")
    account_type=models.CharField( max_length=50,choices=ACCOUNT_CHOICES,default="User")
    # dob=models.DateField(verbose_name="Date of birth")


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

