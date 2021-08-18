from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request,"home/index.html",context)

def show_photos(request):
    context = {}
    return render(request,"media/photos/index.html",context)