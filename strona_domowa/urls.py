from django.urls import path, re_path
from . import views

app_name = 'strona_domowa'

urlpatterns = [
    #/sd/
    path('', views.IndexView.as_view(), name='index'),
    path('omnie/', views.OMnieView.as_view(), name='o_mnie'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    path(r'projekty/', views.ProjektyView.as_view(), name='projekty'),



]

