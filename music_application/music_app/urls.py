from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.user_home_screen, name="home"),
    path("home/<int:id>/", views.user_home_screen, name="playlist"),
    path("home/<int:id>/create_song", views.create_song, name="create_song"),
    path("create_playlist/", views.create_playlist, name="create_playlist"),
    path("remove_playlist/<int:id>/", views.remove_playlist, name="remove_playlist"),
    path("view/", views.view, name="create_playlist"),
]