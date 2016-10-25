from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from apis import mail, sms
from datetime import datetime



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    # def save(self, *args, **kwargs):
    #     super(Comment, self).save(*args, **kwargs)
    #     recipient_list = [self.post.author.email]
    #     mail.send_mail('댓글이 달렸습니다.', '확인해보세요!')
    #     sms.send_sms(['01024956962','01030412840'], self.content)



