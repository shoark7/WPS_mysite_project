from django.db.models.signals import post_save
from django.dispatch import receiver
from apis.mail import send_mail
from blog.models import Comment


# @receiver(post_save, sender=Comment)
# def send_comment_mail(sender, instance, **kwargs):
#     title = '{} 글에 댓글이 달렸습니다.'.format(instance.post.title)
#     content = '{}에 {} 내용이 달렸네요.'.format(
#         instance.created_date.strftime('%Y.%m.%d %H:%M'),
#         instance.content,
#     )
#     send_mail(title, content)

def send_comment_mail(instance, sender=Comment, **kwargs):
    title = '{} 글에 댓글이 달렸습니다.'.format(instance.post.title)
    content = '{}에 {} 내용이 달렸네요.'.format(
        instance.created_date.strftime('%Y.%m.%d %H:%M'),
        instance.content,
    )
    send_mail(title, content)
post_save.connect(send_comment_mail)
