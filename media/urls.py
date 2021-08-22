from django.urls import path

from . import views

urlpatterns = [
    path('videos/', views.video_gallery, name="videos"),
    path('videos/update_video/<str:pk>/',
         views.update_video, name="update_video"),
    path('videos/delete_video/<str:pk>',
         views.delete_video, name="delete_video"),
]
