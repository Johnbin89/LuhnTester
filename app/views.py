from django.shortcuts import render, redirect
from .luhn import find_check_digit, verify_number
from .forms import FindCheckDigitForm, VerifyNumberForm

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST' and 'btn_check_digit' in request.POST:
        digit_form = FindCheckDigitForm(request.POST)
        cardno_form = VerifyNumberForm()
        if digit_form.is_valid():
            string_number = digit_form.cleaned_data['number']
            check_digit = find_check_digit(string_number)
            context.update({'check_digit': check_digit, 'string_number': string_number})
    elif request.method == 'POST' and 'btn_verify' in request.POST:
        digit_form = FindCheckDigitForm()
        cardno_form = VerifyNumberForm(request.POST)
        if cardno_form.is_valid():
            string_number = cardno_form.cleaned_data['card_number']
            validity = verify_number(string_number)
            context.update({'validity': validity, 'string_number': string_number})
    else:
        digit_form = FindCheckDigitForm()
        cardno_form = VerifyNumberForm()
    context['digit_form'],context['cardno_form'] = digit_form, cardno_form
    return render(request, 'index.html', context)
