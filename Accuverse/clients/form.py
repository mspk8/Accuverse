from .models import Clientinfo
from django import forms

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clientinfo
        fiels="__all__"