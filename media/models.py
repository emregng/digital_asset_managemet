from django.db import models
from django.contrib.auth.models import User

from .validators import file_size

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(
        User, null=True, related_name='admin', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=13, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    caption = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    video = models.FileField(upload_to="video/%y", validators=[file_size])
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Photos(models.Model):
    photo = models.ImageField(null=True,blank=True)
    creation_date   = models.DateTimeField(auto_now_add=True)
    creation_user   = models.ForeignKey(User, verbose_name='User', on_delete=models.SET_NULL, null=True, related_name='creation_photo_user')