from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    role = forms.CharField(max_length=50, initial='None')
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']
        # exclude = ()

