from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    section = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'section', 'password1', 'password2']

