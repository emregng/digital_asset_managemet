from django.urls import path

from . import views

urlpatterns = [
    path('videos/', views.video_gallery, name="videos"),
    path('videos/add_video/', views.add_video, name="add_video"),
    path('videos/update_video/<str:pk>/',
         views.update_video, name="update_video"),
    path('videos/delete_video/<str:pk>',
         views.delete_video, name="delete_video"),

    path('audios/', views.audio, name="audios"),
    path('audios/add_audio', views.add_audio, name="add_audio"),
    path('audios/update_audio/<str:pk>/',
         views.update_audio, name="update_audio"),
    path('audios/delete_audio/<str:pk>',
         views.delete_audio, name="delete_audio"),

    path('add-photo/', views.add_photo, name="add-photo"),

]
