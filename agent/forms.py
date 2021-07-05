from django import forms
from simplemathcaptcha.fields import MathCaptchaField

from django import forms
from django.db.models.fields import TextField
# from .models import AgentAccount
from .models import AgentIdentity
from leads.models import QuoteLeads
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

from django.utils.translation import gettext_lazy as _

from configuration.models import SchoolLevel
from configuration.models import AnnualSchoolFees

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields =  ['first_name', 'last_name', 'email', ]

    first_name=forms.CharField(max_length=40,required=True,widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control form-control-custom',}))
    last_name=forms.CharField(max_length=40,required=True,widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control form-control-custom',}))
    phone=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'placeholder':'Phone number','class':'form-control form-control-custom'}))
    email = forms.EmailField(label=_('Email'),widget= forms.EmailInput(attrs={'placeholder':'Enter your email','class':'form-control','id':'email'}),required=True,help_text=_('Required. Enter an existing email address.'))
    
    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))
        return email


# class SignUpForm(forms.Form):
    # phone=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'placeholder':'Phone number','class':'form-control form-control-custom'}))
    
