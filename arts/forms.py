from django.forms import ModelForm
from django import forms
from . models import Contact

class ContactForm(ModelForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control rounded-0 border-top-0 border-end-0 border-start-0', 'name':'name', 'type':'text', 'placeholder':'Full Name', 'type':'name'}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control rounded-0 border-top-0 border-end-0 border-start-0', 'placeholder':'Email', 'type':'email', 'name':'email'}))
    message = forms.CharField(max_length=10000, required = True, widget=forms.Textarea(attrs={'class':'textarea form-control rounded-0 border-top-0 border-end-0 border-start-0', 'name':'message', 'placeholder':'Message', 'rows':'5'}))

    class Meta: 
        model = Contact
        fields = '__all__'
