from django import forms

from .models import Video, Account


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['caption', 'description', 'video', 'tag']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['user']
