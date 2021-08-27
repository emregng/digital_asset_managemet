from django import forms

from .models import *


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['caption', 'description', 'video']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
