from dataclasses import fields
from itertools import product
from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Nuevos_Productos

class Local_Formulario(forms.Form):
    name=forms.CharField(max_length=50, label="Fantasy name")
    CITY = (
        (0, "Select"),
        (1, "Córdoba"),
        (2, "Capital Federal"),
        (3, "Rosario"),
        (4, "Mendoza"),
        (5, "Salta"))
    city= forms.ChoiceField(choices=CITY, required=True, label="In which city the store is?",initial=0)
    address= forms.CharField(max_length=50, label="Enter the address, please")
    mall_number= forms.IntegerField(min_value=0)
    DAYS=(
        (0, "Select"),
        (1, "Monday to friday"),
        (2, "Monday to saturday"),
        (3, "Monday to monday"),
    )    
    opening_hours=forms.ChoiceField(choices=DAYS,required=True, label="Which days does the store open?",initial=0)

class Vendedor_Formulario(forms.Form):
    name= forms.CharField(max_length=30)
    last_name= forms.CharField(max_length=30)
    email= forms.EmailField()
    mall_number= forms.CharField()
    birthday= forms.DateField()

class Producto_Formulario(forms.Form):
    product= forms.CharField(max_length=30, label="Product name")
    prize= forms.FloatField(min_value=0, label="Enter prize, please")
    marcas=(
        (0, 'Select'),
        (1, 'Apple'),
        (2, 'Samsung'),
        (3, 'Huawei'),
        (4, 'Sony')
    )   
    brand= forms.ChoiceField(choices=marcas,required=True, label='Enter brand, please')
    stock= forms.IntegerField(min_value=0, label="Available stock")

class Nuevos_Productos_Formulario(forms.ModelForm):
    class Meta:
        model = Nuevos_Productos
        fields = ['product', 'brand', 'release_date']
        verbose_name_plural = "Nuevos Productos"

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Password', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repeat password', widget=forms.PasswordInput)
    last_name: forms.CharField(label='Last name')
    first_name: forms.CharField(label='Name')
    class Meta:
        model = User                                              
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': 'Username', 'email':'Email','last_name': 'Last name', 'first_name':'Name'}
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    email = forms.EmailField(label='Change email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}