from django import forms
from .models import *


class Request(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['name', 'type', 'request', 'email']
