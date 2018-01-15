from django.urls import path, re_path
from . import views

app_name = 'nowa'

urlpatterns = [
    #/nowa/
    path('', views.index, name='index'),
    #/nowa/71/
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # /nowa/<album_id>/favorite
    re_path(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]

