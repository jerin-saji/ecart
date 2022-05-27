
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))#bootstrap class adding
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})) 
    message =forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))
    