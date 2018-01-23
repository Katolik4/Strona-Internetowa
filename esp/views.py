from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import UserForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Urzadzenie, Gpio
from django.urls import reverse_lazy


#@login_required
class IndexView(generic.ListView):
    template_name = 'esp/index.html'
    context_object_name = 'all_urzadzenia'

    def get_queryset(self):
        return Urzadzenie.objects.all()

class DetailView(generic.DetailView):
    model = Urzadzenie
    context_object_name = 'urzadzenie'
    template_name = 'esp/detail.html'


# URZADZENIE MODEL GENERIC
class UrzadrzenieCreate(CreateView):
    model = Urzadzenie
    fields = ['nr_ser', 'Nazwa', 'Seria']

class UrzadrzenieUpdate(UpdateView):
    model = Urzadzenie
    fields = ['nr_ser', 'Nazwa', 'Seria']

class UrzadrzenieDelete(DeleteView):
    model = Urzadzenie
    success_url = reverse_lazy('esp:index')


# GPIO MODEL GENERIC
class GpioCreate(CreateView):
    model = Gpio
    fields = ['stan', 'opis', 'lista', 'bolean', 'urzadzenie']

    def get_initial(self):
        initial = super(GpioCreate, self).get_initial()
        initial = initial.copy()
        initial['urzadzenie'] = self.kwargs["pk_urzadzenie"]
        return initial

class GpioUpdate(UpdateView):
    model = Gpio
    fields = ['stan', 'opis', 'lista', 'bolean']

class GpioDelete(DeleteView):
    model = Gpio
    context_object_name = 'gpio'

    def get_success_url(self):
        return reverse_lazy( 'esp:detail', kwargs={'pk': self.object.urzadzenie.pk})


# REJESTRACJA NOWEGO USERA
class UserFormView(View):
    form_class = UserForm
    template_name = 'esp/regestration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('esp:index')
        return render(request, self.template_name, {'form': form})



# def index(request):
#     wszyskie_albumy = Urzadzenie.objects.all()
#
#     context = {
#         'wszystkie_albumy': wszyskie_albumy,
#     }
#
#     return render(request,'esp/index.html', context)