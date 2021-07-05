from django import forms
  
from order.models import KYC 
from order.models import Docs
from order.models import Beneficiary
from agent.models import AgentIdentity
from claims.models import Claims
class KYCForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Or to set READONLY
        self.fields["sum_assured"].widget.attrs["readonly"] = True
        
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
     

class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = "__all__"    
        widgets = {
            'beneficiary_dob': forms.DateInput(attrs={'class':'datepicker'}),
        }
        

class AgentIdentityForm(forms.ModelForm):
    class Meta:
        model = AgentIdentity
        fields = "__all__"               
        widgets = {
        } 

class ClaimsForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = "__all__"               
 