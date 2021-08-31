from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

import json
import random

from media.models import *


# Create your views here.


@login_required(redirect_field_name='accounts:login')
def home(request):
    context = {}
    return render(request, "home/index.html", context)


@login_required(redirect_field_name='accounts:login')
def video_market(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    videos = Video.objects.all()

    context = {'videos': videos, 'cartItems': cartItems}
    return render(request, "home/video_market.html", context)


@login_required(redirect_field_name='accounts:login')
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items': items, 'order': order}
    return render(request, 'home/cart.html', context)


@login_required(redirect_field_name='accounts:login')
def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items': items, 'order': order}
    return render(request, 'home/checkout.html', context)


@login_required(redirect_field_name='accounts:login')
def show_photos(request):
    photos = Photos.objects.all()
    if 'shuffle_item' in request.POST:
        photos = sorted(Photos.objects.all().order_by(
            'id'), key=lambda x: random.random())
    elif 'all_item' in request.POST:
        photos = Photos.objects.all()
    elif 'ascending' in request.POST:
        photos = Photos.objects.all().order_by('id')
    elif 'descending' in request.POST:
        photos = Photos.objects.all().order_by('-id')
    context = {'photos': photos}
    return render(request, "media/photos/index.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    video = Video.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, video=video)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    orderItem.save()

    if action == 'remove':
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
