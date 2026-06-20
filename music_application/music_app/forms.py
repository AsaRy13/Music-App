from django import forms

class CreatePlaylist(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    # check = forms.BooleanField()

class CreateSong(forms.Form):
    text = forms.CharField(label="Text", max_length=300)
    file = forms.FileField()