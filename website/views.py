from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
import random
from media.models import Photos
# Create your views here.

@login_required(redirect_field_name='accounts:login')
def home(request):
    context = {}
    return render(request,"home/index.html",context)


@login_required(redirect_field_name='accounts:login')
def show_photos(request):
    photos = Photos.objects.all()
    if 'shuffle_item' in request.POST:
        photos = sorted(Photos.objects.all().order_by('id'), key=lambda x: random.random())
    elif 'all_item' in request.POST:
        photos = Photos.objects.all()
    elif 'ascending' in request.POST:
        photos = Photos.objects.all().order_by('id')
    elif 'descending' in request.POST:
        photos = Photos.objects.all().order_by('-id')
    context = {'photos':photos}
    return render(request,"media/photos/index.html",context)