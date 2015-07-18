from django import forms
from django.forms import ModelForm
from growlerdeals.models import Brewery
from django.core.validators import MinValueValidator, MaxValueValidator



class AddDeal(forms.Form):
    Sunday = forms.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(25)], decimal_places=2, required=False)
    Monday = forms.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(25)], decimal_places=2, required=False)
    Tuesday = forms.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(25)], decimal_places=2, required=False)
    Wednesday = forms.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(25)], decimal_places=2, required=False)
    Thursday = forms.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(25)], decimal_places=2, required=False)
    Friday = forms.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(25)], decimal_places=2, required=False)
    Saturday = forms.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(25)], decimal_places=2, required=False)
 

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	subject = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

class AddBrewery(forms.Form):
    brewery_name=forms.CharField(max_length=50)
    website = forms.CharField(max_length=100, required=False)
    address_line1 =forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=2)
    zip_code = forms.CharField(max_length=10)

class SomethingWrong(forms.Form):
    message = forms.CharField(widget=forms.Textarea, max_length=140)
    email = forms.EmailField(required=False)
    source = forms.CharField(max_length=140, required=False)




