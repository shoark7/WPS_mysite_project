from photo.models import Album, Photo, PhotoDislike, PhotoLike
from photo.forms import PhotoForm
from django.shortcuts import render, redirect

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


def photo_like(request, photo_id):
    user = request.user
    photo = Photo.objects.get(pk=photo_id)
    album_id = photo.album.id

    if PhotoLike.objects.filter(user=user, photo=photo).exists():
        pass
    else:
        PhotoLike.objects.create(
            photo=photo,
            user=user,
        )
    return redirect('photo:album_detail', album_id=album_id)



def photo_dislike(request, photo_id):
    user = request.user
    photo = Photo.objects.get(pk=photo_id)
    album_id = photo.album.id

    if PhotoDislike.objects.filter(user=user, photo=photo).exists():
        pass
    else:
        PhotoDislike.objects.create(
            photo=photo,
            user=user,
        )
    return redirect('photo:album_detail', album_id)

def photo_delete(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    album_id = photo.album.id
    photo.delete()
    return redirect('photo:album_detail', album_id)