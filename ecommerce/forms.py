from django import forms
from django.db.migrations.operations import fields
from django.forms import widgets
from .models import Product, User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'username',
            'first_name',
            'last_name',
            'user_address',
            'email'
            ]
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
            'user_address':forms.Select(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'email'}),
            
        }



class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields=[
           'product_name',
           'description',
           'product_image',
           'product_price',
           'product_category',
           'product_brand',
           'available',
        ]
        widgets={
            'product_name':forms.TextInput(attrs={'class':'form-control','placeholder':'product name'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'product description'}),
           'product_category':forms.Select(attrs={'class':'form-control'}),
           'product_brand':forms.Select(attrs={'class':'form-control'}),
        }
