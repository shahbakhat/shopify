from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomerRegistrationForm(UserCreationForm):
  password1 = forms.CharField(label='Password', 
                              widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  password2 = forms.CharField(label='Confirm Password(Again)', 
                              widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    labels = {'email': 'Email'}
    widgets= {'username': forms.TextInput(attrs= {'class': 'form-control'})}

class CustomerLoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
