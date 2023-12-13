# forms.py
from django import forms
from .models import BannerSettings


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Поиск', max_length=100)


class BannerSettingsForm(forms.ModelForm):
    class Meta:
        model = BannerSettings
        fields = ['rotation_interval']
