from django.urls import path, re_path
from . import views

app_name = 'esp'

urlpatterns = [
    #/nowa/
    path('', views.IndexView.as_view(), name='index'),
    #/esp/71/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/esp/urzadzenie/add
    re_path(r'urzadzenie/add/$', views.UrzadrzenieCreate.as_view(), name='urzadzenie-add'),
    re_path(r'urzadzenie/(?P<pk>[0-9]+)/$', views.UrzadrzenieUpdate.as_view(), name='urzadzenie-update'),
    re_path(r'(?P<pk_urzadzenie>[0-9]+)/gpio/(?P<pk>[0-9]+)/$', views.GpioUpdate.as_view(), name='gpio-update'),
    re_path(r'(?P<pk>[0-9]+)/gpio/add/$', views.GpioCreate.as_view(), name='gpio-add'),
    re_path(r'urzadzenie/(?P<pk>[0-9]+)/delete/$', views.UrzadrzenieDelete.as_view(), name='urzadzenie-delete'),
    # /nowa/<album_id>/favorite
    #re_path(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]

