# import email
# from email import message
from django import forms
# from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone= forms.CharField(max_length=15)
    message= forms.CharField(widget=forms.Textarea)

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.CharField(validators=[EmailValidator()])
#     phone= forms.CharField(max_length=15)
#     message= forms.CharField(widget=forms.Textarea)

