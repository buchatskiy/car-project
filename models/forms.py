# -*- coding: utf-8 -*-
from django import forms
from models import Brand, Model


class MyForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), label="Выберете производителя:",
                                   widget=forms.Select(attrs={"onChange": 'submit()'}),
                                   required=True)
    model = forms.ModelChoiceField(queryset=Model.objects.all(), label="Выберете модель:", required=True)
    run = forms.CharField(required=True, label="Введите пробег в км.:")