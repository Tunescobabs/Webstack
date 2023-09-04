
from django import forms
from .models import User, Question

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email']

class AnswerForm(forms.Form):
    option = forms.ChoiceField(widget=forms.RadioSelect)
    