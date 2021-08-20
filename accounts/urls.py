from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views




urlpatterns = [
    path('login/', views.view_login,name = "login"),
    path('logout/', views.logout_view,name = "logout"),

]
