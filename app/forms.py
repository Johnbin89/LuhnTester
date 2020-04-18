from django import forms
from django.core.validators import RegexValidator

numeric = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')


class FindCheckDigitForm(forms.Form):
    number = forms.CharField(validators=[numeric])
    
class VerifyNumberForm(forms.Form):
    card_number = forms.CharField(max_length=16, min_length=16, validators=[numeric])