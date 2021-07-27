from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.widgets import PasswordInput, TextInput

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=PasswordInput(attrs={'class':'form-control mb-2'}))
    password2=forms.CharField(label='Confirm Password',widget=PasswordInput(attrs={'class':'form-control mb-2'}))
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
        labels={'first_name': 'First Name', 'last_name':'Last Name','email':'Email','username':'User Name'}
        widgets={ 
                'first_name':forms.TextInput(attrs={'class':'form-control mb-2'}),
                'last_name':forms.TextInput(attrs={'class':'form-control mb-2'}),
                'email':forms.EmailInput(attrs={'class':'form-control mb-2'}),
                'username':forms.TextInput(attrs={'class':'form-control mb-2'}),
            

        }

class UserLogin(AuthenticationForm):
    username=UsernameField(label='User Name',widget=forms.TextInput(attrs={
        'class':'form-control mb-2',
        'autofocus':True,

    }))

    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={
        'class':'form-control mb-2'
    }))
