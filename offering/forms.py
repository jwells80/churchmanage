from django import forms

class paymenttypeForm(forms.Form):
    payment_type = forms.CharField(max_length=200)

class fundForm(forms.Form):
    fund = forms.CharField(max_length=200)