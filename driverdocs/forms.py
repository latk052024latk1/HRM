from django.forms import ModelForm, TextInput, EmailInput, FileInput

from django import forms
from .models import Drivers, Documents

class DocsForm(ModelForm):
    class Meta:
        model = Documents
        fields = ['doc_number', 'doc_category', 'doc_given', 'doc_expire', 'doc_path']

        widgets = {
            'doc_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'საბუთის ნომერი'
                }),

            'doc_category': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; height:100%;',
                'placeholder': ''
                }),

            'doc_given': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'გაცემის თარიღი'
                }),

            'doc_expire': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'მოქმედების ვადა'
                }),
            'doc_path': forms.FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'ფაილი'

                })

        }


class DriverForm(ModelForm):
    class Meta:
        model = Drivers
        fields = ['dr_personal', 'dr_name', 'dr_surname', 'dr_email','birth_date']

        widgets = {
            'dr_personal': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'პირადი ნომერი'
                }),
            'dr_name': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'სახელი'
                }),

            'dr_surname': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'გვარი'
                }),
            'dr_email': forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'

                }),
            'birth_date': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'დაბადების თარიღი'
                })

        }


class DocsForm1(ModelForm):
    class Meta:
        model = Documents
        fields = ['doc_number', 'doc_given', 'doc_expire', 'doc_path']


        widgets = {
            'doc_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'საბუთის ნომერი'
                }),


            'doc_given': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'გაცემის თარიღი'
                }),

            'doc_expire': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'მოქმედების ვადა'
                }),
            'doc_path': forms.FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'ფაილი'

                })

        }
