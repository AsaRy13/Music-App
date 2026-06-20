from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import MusicList, Item
from .forms import *

# Create your views here.
def index(response):
    return render(response, "music_app/startpage.html", {})

def user_home_screen(response, id=0):
    if id != 0:
        ls = MusicList.objects.get(id=id)

        if ls in response.user.musiclist.all():
            return render(response, "music_app/list.html", {"ls": ls})
    return render(response, "music_app/home.html", {})

def create_playlist(response):
    if response.method == "POST":
        form = CreatePlaylist(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            m = MusicList(name=n)
            m.save()
            response.user.musiclist.add(m)
        
        return HttpResponseRedirect("/view")
    else:
        form = CreatePlaylist()
    return render(response, "music_app/createplaylist.html", {"form": form})

def remove_playlist(response, id):
    MusicList.objects.get(id=id).delete()
    return HttpResponseRedirect("/view")

def view(response):
    return render(response, "music_app/view.html", {})

def create_song(response, id):
    ls = MusicList.objects.get(id=id)
    if response.method == "POST":
        form = CreateSong(response.POST, response.FILES)

        if form.is_valid():
            n = form.cleaned_data["text"]
            f = form.cleaned_data["file"]
            ls.item_set.create(text=n, file=f)

        return HttpResponseRedirect("/home/%i" % id)
    else:
        form = CreateSong()
    return render(response, "music_app/createsong.html", {"form": form, "ls": ls})