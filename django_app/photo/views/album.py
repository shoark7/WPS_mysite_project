from photo.models import Album, Photo, PhotoDislike, PhotoLike
from photo.forms import AlbumForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def album_add(request):
    context = {}
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            user = request.user

            album = Album.objects.create(
                title=title,
                owner=user,
                description=description,
            )
            messages.info(request, '앨범이 생성되었습니다.')
            return redirect('photo:album_list')
        else:
            context['form'] = form
    else:
        form = AlbumForm()
        context['form'] = form
    return render(request, 'photo/album_add.html', context)


def album_list(request):
    albums = Album.objects.filter(owner=request.user)
    return render(request, 'photo/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    the_album = get_object_or_404(Album, pk=album_id)
    all_photos = the_album.photo_set.all()
    context = {
        'album': the_album,
        'photos': all_photos,
    }
    template_file = 'photo/ajx_album_detail.html'
    # template_file = 'photo/album_detail.html'

    return render(request, template_file, context)


def album_delete(request):
    print(request.POST['album_id'])
    if request.method == 'POST':
        try:
            album_id = request.POST['album_id']
        except KeyError:
            pass
        else:
            album_to_be_deleted = Album.objects.get(pk=album_id)
            album_to_be_deleted.delete()
    return redirect('photo:album_list')
