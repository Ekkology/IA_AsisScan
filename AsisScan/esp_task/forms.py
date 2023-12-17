from django import forms
from .models import camaras


class CamarasForm(forms.ModelForm):
    class Meta:
        model = camaras
        fields = ['modelo', 'lugar']