from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from .forms import VideoForm
from .models import *
# Create your views here.


@login_required(redirect_field_name='accounts:login')
def video_gallery(request):
    all_video = Video.objects.all()
    if request.method == "POST":
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media:videos')
    else:
        form = VideoForm()

    total_videos = all_video.count()

    context = {'form': form, 'all_video': all_video,
               'total_videos': total_videos}

    return render(request, 'media/videos/videos.html', context)

@login_required(redirect_field_name='accounts:login')
def audio(request):
    audio = Audio.objects.all()
    context={"audio":audio}
    return render(request,"media/audios/audios.html",context)


def update_video(request, pk):

    video = Video.objects.get(id=pk)
    form = VideoForm(instance=video)

    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('media:videos')

    context = {'form': form}

    return render(request, 'media/videos/videos.html', context)


def delete_video(request, pk):
    video = Video.objects.get(id=pk)

    if request.method == "POST":
        video.delete()
        return redirect('media:videos')

    context = {'item': video}
    return render(request, 'media/videos/deleteVideo.html', context)


def add_photo(request):
    if request.method == 'POST':
        data = request.FILES['file']
        Photos.objects.create(photo=data, creation_user=request.user)

    return HttpResponse('Ok')
