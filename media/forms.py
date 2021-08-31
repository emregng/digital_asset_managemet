from django import forms

from .models import *


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['caption', 'description', 'video', 'price']


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'artist', 'image', 'audio_file', 'price']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
