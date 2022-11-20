from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from . import models


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

# ########## LOGIN & REGISTER ###########


class Login(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class RegistroUsuario(FormView):
    template_name = 'core/registrar.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroUsuario, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegistroUsuario, self).get(*args, **kwargs)


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


# ########## CRUD MARCA CARRO ###########
class ListaMarcas(ListView):
    model = models.MarcaCarro
    context_object_name = 'marcas'
    template_name = 'core/marcas.html'


class CadastrarMarca(CreateView):
    model = models.MarcaCarro
    fields = '__all__'
    template_name = 'core/cadastrar_marca.html'
    success_url = reverse_lazy('marcas')

    def form_valid(self, form):
        return super(CadastrarMarca, self).form_valid(form)


class EditarMarca(UpdateView):
    model = models.MarcaCarro
    fields = '__all__'
    template_name = 'core/editar_marca.html'
    success_url = reverse_lazy('marcas')


class RemoverMarca(DeleteView):
    model = models.MarcaCarro
    context_object_name = 'marca'
    template_name = 'core/remover_marca.html'
    success_url = reverse_lazy('marcas')
