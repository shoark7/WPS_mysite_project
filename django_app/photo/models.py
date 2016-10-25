from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Album title : {}".format(self.title[:10])

class Photo(models.Model):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='photo')

    def __str__(self):
        return "Photo title : {}".format(self.title[:10])
