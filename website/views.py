from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(redirect_field_name='accounts:login')
def home(request):
    context = {}
    return render(request,"home/index.html",context)

@login_required(redirect_field_name='accounts:login')
def show_photos(request):
    context = {}
    return render(request,"media/photos/index.html",context)