from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from django.forms import ModelForm
from .models import member, child


class memberForm(ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Div('first_name', css_class='col-4'),
            Div('spouse', css_class='col-4'),
            Div('last_name', css_class='col-4'),
        css_class='row'),

    )
    class Meta:
        model = member
        fields = '__all__'


class childForm(ModelForm):
    class Meta:
        model = child
        fields = ['name']