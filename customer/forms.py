from django import forms
  
from order.models import KYC 
from order.models import Docs
from order.models import Beneficiary
from agent.models import AgentIdentity
  
class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = "__all__"
        widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}),
            'nominee_dob': forms.DateInput(attrs={'class':'datepicker'}),
        }
  
class DocsForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = "__all__"        

class DocsForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = "__all__"    
class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = "__all__"    

class AgentIdentityForm(forms.ModelForm):
    class Meta:
        model = AgentIdentity
        fields = "__all__"               
        widgets = {
        } 
 