from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify = forms.EmailField(label='Enter Your Email')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        verify = all_clean['verify']

        if email != verify:
            raise forms.ValidationError("EMAIL NOT MATCHING")
