from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('photos/', views.show_photos, name="photos"),
    path('video_market/', views.video_market, name="video_market"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
]
