from django import forms
from .models import Clientinfo, Service

class ClientForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Clientinfo
        fields = '__all__'
