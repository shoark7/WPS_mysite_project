from django.conf.urls import url
from photo import views


urlpatterns = [
    url(r'^photo_add/(?P<album_id>\d+)/$', views.photo_add, name='photo_add'),
    # url(r'^photo_like/(?P<photo_id>\d+)/$', views.photo_like, name='photo_like'),
    # url(r'^photo_dislike/(?P<photo_id>\d+)/$', views.photo_dislike, name='photo_dislike'),
    url(r'^photo_like/(?P<photo_id>\d+)/(?P<like_type>\w+)/$', views.photo_like, name='photo_like'),
    url(r'^photo_delete/(?P<photo_id>\d+)/$', views.photo_delete, name='photo_delete'),

    url(r'^album_add/$', views.album_add, name='album_add'),
    url(r'^$', views.album_list, name='album_list'),
    url(r'^album_detail/(?P<album_id>\d+)/$', views.album_detail, name='album_detail'),
    # url(r'^album_delete/(?P<album_id>\d+)/$', views.album_delete, name='album_delete'),
    url(r'^album_delete/$', views.album_delete, name='album_delete'),


]
