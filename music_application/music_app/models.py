from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MusicList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="musiclist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    musicList = models.ForeignKey(MusicList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    file = models.FileField(upload_to="uploads/")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text