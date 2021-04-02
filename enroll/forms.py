from django import forms
from django.core import validators
from enroll.models import User
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','password','email']
        help_text={'name':'Enter Your Full Name'}
        labels={'name':'Enter name Ankesh','password':'Enter Password'}
        widgets={'password':forms.PasswordInput(),
        'name':forms.TextInput()}
