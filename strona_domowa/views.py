from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from .models import Projekt, Okno

#from .forms import UserForm


from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View

class IndexView(generic.View):
    template_name = 'strona_domowa/index.html'

    def get(self, request):
        return render(request, self.template_name)

class ProjektyView(generic.ListView):
    template_name = 'strona_domowa/projekty.html'
    context_object_name = "all_projekty"

    def get_queryset(self):
        return Projekt.objects.all()

class OMnieView(View):
    model = Projekt

    template_name = 'strona_domowa/omnie.html'
    context_object_name = "projekt"

    def get_object(self):
        return get_object_or_404(Projekt, pk=1)

    def get(self, request):
        return render(request, self.template_name, {'projekt':get_object_or_404(Projekt, pk=1)})








class DetailView(generic.DetailView):
    model = Projekt
    context_object_name = "projekt"
    template_name = 'strona_domowa/detail.html'


