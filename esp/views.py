from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Urzadzenie, Gpio
from django.urls import reverse_lazy



class IndexView(generic.ListView):
    template_name = 'esp/index.html'
    context_object_name = 'all_urzadzenia'

    def get_queryset(self):
        return Urzadzenie.objects.all()

class DetailView(generic.DetailView):
    model = Urzadzenie
    context_object_name = 'urzadzenie'
    template_name = 'esp/detail.html'

class UrzadrzenieCreate(CreateView):
    model = Urzadzenie
    fields = ['nr_ser', 'Nazwa', 'Seria']

class UrzadrzenieUpdate(UpdateView):
    model = Urzadzenie
    fields = ['nr_ser', 'Nazwa', 'Seria']

class UrzadrzenieDelete(DeleteView):
    model = Urzadzenie
    success_url = reverse_lazy('esp:index')



class GpioCreate(CreateView):
    model = Gpio
    #model.urzadzenie = '3'
    fields = ['stan', 'opis', 'lista', 'bolean', 'urzadzenie']

class GpioUpdate(UpdateView):
    model = Gpio
    fields = ['stan', 'opis', 'lista', 'bolean']

class GpioDelete(DeleteView):
    model = Gpio
    success_url = reverse_lazy('esp:index')





# def index(request):
#     wszyskie_albumy = Urzadzenie.objects.all()
#
#     context = {
#         'wszystkie_albumy': wszyskie_albumy,
#     }
#
#     return render(request,'esp/index.html', context)