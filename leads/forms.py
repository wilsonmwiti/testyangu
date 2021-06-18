from django import forms
from django.db.models.fields import CharField
from simplemathcaptcha.fields import MathCaptchaField

from policies.models import SchoolLevel
from policies.models import AnnualSchoolFees

class QuoteForm(forms.Form):
    name=forms.CharField(max_length=40,required=True)
    email=forms.EmailField(max_length=254,required=True,)
    phone=forms.IntegerField(required=True,)
    dob=forms.DateField(widget=forms.TextInput(attrs={'type': 'date','max':'2005-01-02','min':'1962-01-01'}))
    fees=forms.ModelChoiceField(queryset=AnnualSchoolFees.objects.all(),to_field_name="fees")
    school_level=forms.ModelChoiceField(queryset=SchoolLevel.objects.all(),to_field_name='school_level')
    years=forms.IntegerField(required=True,)
    captcha = MathCaptchaField()