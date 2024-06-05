from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from users.models import User
from django import forms
from business.forms import *
from django.forms import ModelForm, TextInput, EmailInput, FileInput, Select

class UserChangeForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'pass', 'type':'password','style': 'max-width: 300px', 'align':'center', 'placeholder':'პაროლი'}),
    )


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'მომხმარებლის სახელი'
                }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'სახელი'
                }),

            'last_name': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'გვარი'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'ელ-ფოსტა'
                }),
            'password': forms.PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'id':'id_password',
                'placeholder': 'პაროლი'
                }),
            

        }



class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ABC', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ABC',
            'id': 'hi',
        }
))

    class Meta:
        model = User
        fields = ('username', 'password')

class formCreateU(ModelForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'pass', 'type':'password','style': 'max-width: 300px', 'align':'center', 'placeholder':'პაროლი'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'pass', 'type':'password','style': 'max-width: 300px', 'align':'center', 'placeholder':'გაიმეორეთ პაროლი'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'მომხმარებლის სახელი'
                }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'სახელი'
                }),

            'last_name': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'გვარი'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'ელ-ფოსტა'
                }),
            'password1': forms.PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'id':'id_password1',
                'placeholder': 'პაროლი'
                }),
            'password2': forms.PasswordInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;',
                'id':'id_password2',
                'placeholder': 'გაიმეორეთ პაროლი'
                }),
            

        }

