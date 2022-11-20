from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from . import models


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


# ########## CRUD CARRO ###########
class ListaCarros(ListView):
    model = models.Carro
    context_object_name = 'carros'
    template_name = 'core/carros.html'


class CadastrarCarro(CreateView):
    model = models.Carro
    fields = '__all__'
    template_name = 'core/cadastrar_carro.html'
    success_url = reverse_lazy('carros')

    def form_valid(self, form):
        return super(CadastrarCarro, self).form_valid(form)


class VerCarro(DetailView):
    model = models.Carro
    context_object_name = 'carro'
    template_name = 'core/carro.html'


class EditarCarro(UpdateView):
    model = models.Carro
    fields = '__all__'
    template_name = 'core/editar_carro.html'
    success_url = reverse_lazy('carros')


class RemoverCarro(DeleteView):
    model = models.Carro
    context_object_name = 'carro'
    template_name = 'core/remover_carro.html'
    success_url = reverse_lazy('carros')
