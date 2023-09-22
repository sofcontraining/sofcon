from django import forms
from . models import Contactus

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['name', 'contact', 'email', 'course', 'comment']