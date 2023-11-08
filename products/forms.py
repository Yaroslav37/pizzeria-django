# forms.py
from django import forms

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Поиск', max_length=100)
