from django import forms

class paymenttypeForm(forms.Form):
    payment_type = forms.CharField(max_length=20)