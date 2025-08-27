from django import forms
from.models import Workplace

class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = ['number', 'type', 'status', 'employee']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
