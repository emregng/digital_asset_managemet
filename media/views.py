from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from .forms import VideoForm, AudioForm
from .models import *
# Create your views here.


@login_required(redirect_field_name='accounts:login')
def video_gallery(request):
    all_video = Video.objects.all()

    total_videos = all_video.count()

    context = {'all_video': all_video,
               'total_videos': total_videos}

    return render(request, 'media/videos/videos.html', context)


def add_video(request):

    form = VideoForm()

    if request.method == 'POST':
        form = VideoForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media:videos')
        else:
            form = VideoForm()

    context = {'form': form}

    return render(request, 'media/videos/addVideo.html', context)


def update_video(request, pk):

    video = Video.objects.get(id=pk)
    form = VideoForm(instance=video)

    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('media:videos')

    context = {'form': form}

    return render(request, 'media/videos/updateVideo.html', context)


def delete_video(request, pk):
    video = Video.objects.get(id=pk)

    if request.method == "POST":
        video.delete()
        return redirect('media:videos')

    context = {'item': video}
    return render(request, 'media/videos/deleteVideo.html', context)


@login_required(redirect_field_name='accounts:login')
def audio(request):
    audio = Audio.objects.all()
    context = {"audio": audio}
    return render(request, "media/audios/audios.html", context)


def add_audio(request):

    form = AudioForm()

    if request.method == 'POST':
        form = AudioForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media:audios')
        else:
            form = AudioForm()

    context = {'form': form}

    return render(request, 'media/audios/addAudio.html', context)


def update_audio(request, pk):

    audio = Audio.objects.get(id=pk)
    form = AudioForm(instance=audio)

    if request.method == 'POST':
        form = AudioForm(request.POST, instance=audio)
        if form.is_valid():
            form.save()
            return redirect('media:audios')

    context = {'form': form}

    return render(request, 'media/audios/updateAudio.html', context)


def delete_audio(request, pk):
    audio = Audio.objects.get(id=pk)

    if request.method == "POST":
        audio.delete()
        return redirect('media:audios')

    context = {'item': audio}
    return render(request, 'media/audios/deleteAudio.html', context)


def add_photo(request):
    if request.method == 'POST':
        data = request.FILES['file']
        Photos.objects.create(photo=data, creation_user=request.user)

    return HttpResponse('Ok')
