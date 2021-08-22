from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.view_login, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.view_register, name="register"),
    path('settings/', views.accountSettings, name="settings"),
]
