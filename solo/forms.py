from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


class BasicForm(forms.Form):
    field1 = forms.CharField()
    field2 = forms.CharField()
    # result_field = forms.CharField()
