from django.db import models
from django.contrib.auth.models import User

from .validators import file_size

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    caption = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    video = models.FileField(upload_to="video/%y", validators=[file_size])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption


class Photos(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_user = models.ForeignKey(
        User, verbose_name='User', on_delete=models.SET_NULL, null=True, related_name='creation_photo_user')

    def __str__(self):
        return self.name


class Audio(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    audio_file = models.FileField(upload_to='audios/%y', blank=True, null=True)
    price = models.FloatField(null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Order(models.Model):

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)

    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    video = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.video.price * self.quantity
        return total
