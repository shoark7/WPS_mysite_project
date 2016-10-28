from django.shortcuts import get_object_or_404, redirect
from ..models import Photo, PhotoDislike, PhotoLike
from django.urls import reverse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

__all__ = ['photo_like', ]


@require_POST
@csrf_exempt
def photo_like(request, photo_id, like_type='like'):
    photo = Photo.objects.get(pk=photo_id)
    album = photo.album
    user = request.user
    like_model = PhotoLike if like_type == 'like' else PhotoDislike
    opposite_model = PhotoLike if like_model == PhotoDislike else PhotoDislike
    next_path = request.GET.get('next', reverse('photo:album_detail', kwargs={'album_id': album.pk}))

    user_model_exists = like_model.objects.filter(
        user=user,
        photo=photo,
    )
    is_delete = False

    if user_model_exists.exists():
        user_model_exists.delete()
        is_delete = True
    else:
        like_model.objects.create(
            user=user,
            photo=photo,
        )
        opposite_model.objects.filter(
            user=user,
            photo=photo,
        ).delete()
        # msg = 'created'
    ret = {
        'like_count': photo.like_users.count(),
        'dislike_count': photo.dislike_users.count(),
        'user_like': True if photo.like_sers.filter(id=request.user.id).exists() else False,
        'user_dislike': True if photo.dislike_users.filter(id=request.user.pk).exists() else False,
    }


    return HttpResponse(json.dumps(ret), content_type='application/json')
