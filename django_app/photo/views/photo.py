from photo.models import Album, Photo, PhotoDislike, PhotoLike
from photo.forms import PhotoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse

def photo_add(request, album_id):
    album = Album.objects.get(pk=album_id)
    user = request.user
    context = {}


    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():

            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            img = form.cleaned_data['img']
            photo = Photo.objects.create(
                owner=user,
                album=album,
                title=title,
                description=description,
                img=img,
            )
            return redirect('photo:album_detail', album_id=album.id)
        else:
            context['form'] = form
    else:
        form = PhotoForm()
        context['form'] = form
    return render(request, 'photo/photo_add.html', context)


# def photo_like(request, photo_id):
#     user = request.user
#     photo = Photo.objects.get(pk=photo_id)
#     album_id = photo.album.id
#
#     if PhotoLike.objects.filter(user=user, photo=photo).exists():
#         pass
#     else:
#         PhotoLike.objects.create(
#             photo=photo,
#             user=user,
#         )
#     return redirect('photo:album_detail', album_id=album_id)
#
#
#
# def photo_dislike(request, photo_id):
#     user = request.user
#     photo = Photo.objects.get(pk=photo_id)
#     album_id = photo.album.id
#
#     if PhotoDislike.objects.filter(user=user, photo=photo).exists():
#         pass
#     else:
#         PhotoDislike.objects.create(
#             photo=photo,
#             user=user,
#         )
#     return redirect('photo:album_detail', album_id)

def photo_delete(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    album_id = photo.album.id
    photo.delete()
    return redirect('photo:album_detail', album_id)


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

    if user_model_exists.exists():
        user_model_exists.delete()
    else:
        like_model.objects.create(
            user=user,
            photo=photo,
        )
        opposite_model.objects.filter(
            user=user,
            photo=photo,
        ).delete()

    return redirect(next_path)

    # 1. 좋아요 또는 싫어요를 처음 눌렀을 때
    # 2. 누른 버튼을 또 한 번 눌렀을 때
    # 3. '좋아요 -> 싫어요', '싫어요 -> 좋아요'로 갈아탈 때


























#
#
# @require_POST
# def photo_like(request, pk, like_type='like'):
#     """
#     1. 요청한 사람이 이미 눌렀는가?
#     2.
#     """
#
#
#     photo = get_object_or_404(Photo, pk=pk)
#     album = photo.album
#     next_path = request.GET.get('next', reverse('photo:album_detail', kwargs={'pk': album.pk}))
#     like_model = PhotoLike if like_type == 'like' else PhotoDislike
#     opposite_model = PhotoDislike if like_type == 'like' else PhotoLike
#
#     user_like_exist = like_model.objects.filter(
#         user=request.user,
#         photo=photo,
#     )
#
#     if user_like_exist.exists():
#         user_like_exist.delete()
#     else:
#         like_model.objects.create(
#             user=request.user,
#             photo=photo,
#         )
#         opposite_model.objects.filter(
#             user=request.user,
#             photo=photo
#         ).delete()
#
#     return redirect(next_path)