from django import forms
from django.db.models.fields import CharField
from simplemathcaptcha.fields import MathCaptchaField

class ContactUsForm(forms.Form):
    name=forms.CharField(max_length=40,required=True,widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control form-control-custom',}))
    email=forms.EmailField(max_length=254,required=True,widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control form-control-custom'}))
    phone=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'placeholder':'Phone number','class':'form-control form-control-custom'}))
    subject=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Subject','class':'form-control form-control-custom'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message','class':'form-control form-control-custom',}))
    captcha = MathCaptchaField()