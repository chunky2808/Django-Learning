from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    phoneno = forms.DecimalField(min_value=999999999,max_digits=10, required=True, widget=forms.NumberInput())
    class Meta:
        model = User
        fields = ('username', 'email','phoneno', 'password1', 'password2')