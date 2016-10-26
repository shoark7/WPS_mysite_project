from django.conf.urls import url
from photo import views


urlpatterns = [
    url(r'^photo_add/(?P<album_id>\d+)/$', views.photo_add, name='photo_add'),
    url(r'^album_add/$', views.album_add, name='album_add'),
    url(r'^album_list/$', views.album_list, name='album_list'),
    url(r'^album_detail/(?P<album_id>\d+)/$', views.album_detail, name='album_detail'),

]
