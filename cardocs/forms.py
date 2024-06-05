from django.forms import ModelForm
from django import forms
from .models import *


class CarForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['car_vin', 'car_reg_number']

        widgets = {
            'car_vin': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'მანქანის VIN'
                }),

            'car_reg_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; height:100%;',
                'placeholder': 'სახელმწიფო ნომერი'
                }),

            }
        
class CarDocsForm(ModelForm):
    class Meta:
        model = CarDocuments
        fields = ['car_doc_number', 'car_doc_category', 'car_doc_given', 'car_doc_expire', 'car_doc_path']

        widgets = {
            'car_doc_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'დოკუმენტის ნომერი'
                }),

            'car_doc_category': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; height:100%;',
                'placeholder': ''
                }),

            'car_doc_given': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'გაცემის თარიღი'
                }),
            'car_doc_expire': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'მოქმედების ვადა'
                }),

            'car_doc_path': forms.FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'ფაილი'

                })

        }


class CarDocsUForm(ModelForm):
    class Meta:
        model = CarDocuments
        fields = ['car_doc_number', 'car_doc_given', 'car_doc_expire', 'car_doc_path']

        widgets = {
            'car_doc_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'დოკუმენტის ნომერი'
                }),

            'car_doc_given': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'გაცემის თარიღი'
                }),
            'car_doc_expire': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'მოქმედების ვადა'
                }),

            'car_doc_path': forms.FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'ფაილი'

                })

        }


class TrailerForm(ModelForm):
    class Meta:
        model = Trailers
        fields = ['trailer_vin', 'trailer_reg_number']

        widgets = {
            'trailer_vin': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'ტრაილერის VIN'
                }),

            'trailer_reg_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; height:100%;',
                'placeholder': 'სახელმწიფო ნომერი'
                }),

            }


class TrailerDocsForm(ModelForm):
    class Meta:
        model = TrailerDocuments
        fields = ['trailer_doc_number', 'trailer_doc_category', 'trailer_doc_given',
                  'trailer_doc_expire', 'trailer_doc_path']

        widgets = {
            'trailer_doc_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'დოკუმენტის ნომერი'
                }),

            'trailer_doc_category': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; height:100%;',
                'placeholder': ''
                }),

            'trailer_doc_given': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'გაცემის თარიღი'
                }),
            'trailer_doc_expire': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'მოქმედების ვადა'
                }),

            'trailer_doc_path': forms.FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'ფაილი'

                })

        }


class TrailerDocsUForm(ModelForm):
    class Meta:
        model = TrailerDocuments
        fields = ['trailer_doc_number', 'trailer_doc_given', 'trailer_doc_expire', 'trailer_doc_path']

        widgets = {
            'trailer_doc_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'დოკუმენტის ნომერი'
                }),

            'trailer_doc_given': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'გაცემის თარიღი'
                }),
            'trailer_doc_expire': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'მოქმედების ვადა'
                }),

            'trailer_doc_path': forms.FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;height:100%;',
                'placeholder': 'ფაილი'

                })

        }
