from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Album, Piosenka

def index(request):
    wszyskie_albumy = Album.objects.all()

    context = {
        'wszystkie_albumy': wszyskie_albumy,
    }

    return render(request,'nowa/index.html', context)

def detail(request, album_id):
    #return HttpResponse("<h2>Szczegoly dla albumu id: "+str(album_id)+"</h2>")

    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Nie ma takiej strony")

    album = get_object_or_404(Album, pk=album_id)
    context = {
        'album': album,
    }

    return render(request,'nowa/detail.html', context)

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.piosenka_set.get(pk = request.POST['song'])
    except (KeyError, Piosenka.DoesNotExist):
        return render(request, 'nowa/detail.html', {
            'album' : album,
            'error_message' : "nie wybrales piosenki",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'nowa/detail.html', {'album' : album})