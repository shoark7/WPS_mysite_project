from django.db import models
from member.models import MyUser


class Video(models.Model):
    kind = models.CharField(max_length=100)
    user = models.ManyToManyField(MyUser)
    youtube_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    thumbnail = models.URLField(blank=True)

    def __str__(self):
        return self.title
