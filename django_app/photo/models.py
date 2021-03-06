from django.conf import settings
# 1.
from django.db import models
import os
from mysite.utils.models import BaseModel
# 2. from django.contrib.auth import get_user_model

class Album(BaseModel):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Album title : {}".format(self.title[:10])


class Photo(BaseModel):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='photo')
    # 이미지 섬네일 만들기
    img_thumbnail = models.ImageField(upload_to='photo/thumbnail', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        through='PhotoLike',
                                        related_name='photo_set_like_users',
                                        )
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           through='PhotoDislike',
                                           related_name='photo_set_dislike_users')

    def __str__(self):
        return "Photo title : {}".format(self.title[:10])

    def save(self, *args, **kwargs):
        image_changed = False

        # save전, img필드의 내용이 변했는지 확인
        # 기존에 DB에 저장되어있을 경우에만 지정(self.pk가 없을경우 에러)
        if self.pk:
            ori = Photo.objects.get(pk=self.pk)
            if ori.img != self.img:
                image_changed = True

        # img는 있는데 img_thumbnail은 없을 경우
        if self.img and not self.img_thumbnail:
            image_changed = True

        super().save(*args, **kwargs)
        if image_changed:
            self.make_thumbnail()

    # def url_thumbnail(self):
    #     if self.img_thumbnail:
    #         return self.img_thumbnail.url
    #     else:
    #         return ""

    def url_thumbnail(self):
        return self.url_field('img_thumbnail', default='/static/img/default.jpg')


    def make_thumbnail(self):
        import os
        from PIL import Image, ImageOps
        from io import BytesIO
        from django.core.files.base import ContentFile
        from django.core.files.storage import default_storage

        size = (300, 300)
        # Default storage에서 FileField내용 읽어오기
        f = default_storage.open(self.img)
        print('f : %s' % f)

        # Image.open으로 파일을 Image인스턴스화 (image)
        image = Image.open(f)
        # Image.format은 JPEG, PNG, BMP등 포맷정보를 나타냄
        ftype = image.format
        print('ftype : %s' % ftype)

        # ImageOps.fit메서드를 이용해서 썸네일이미지 생성
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        # 기존에 있던 img의 경로와 확장자를 가져옴
        path, ext = os.path.splitext(self.img.name)
        name = os.path.basename(path)

        # 기존파일명_thumb.확장자 형태가 됨
        thumbnail_name = '%s_thumb%s' % (name, ext)

        # 임시 파일로 취급되는 객체 생성
        temp_file = BytesIO()
        image.save(temp_file, ftype)
        temp_file.seek(0)

        # img_thumbnail필드에 해당 파일내용을 저장
        # Django의 FileField에 내용을 저장할때는 ContentFile형식이어야 함
        content_file = ContentFile(temp_file.read())
        self.img_thumbnail.save(thumbnail_name, content_file)

        # 열었던 파일 닫아줌
        temp_file.close()
        content_file.close()
        f.close()
        return True



class PhotoLike(BaseModel):

    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class PhotoDislike(BaseModel):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
