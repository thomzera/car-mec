from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
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
class ListaCarros(LoginRequiredMixin, ListView):
    model = models.Carro
    paginate_by = 10
    context_object_name = 'carros'
    template_name = 'core/carros.html'


class CadastrarCarro(LoginRequiredMixin, CreateView):
    model = models.Carro
    fields = '__all__'
    template_name = 'core/cadastrar_carro.html'
    success_url = reverse_lazy('carros')

    def form_valid(self, form):
        return super(CadastrarCarro, self).form_valid(form)


class VerCarro(LoginRequiredMixin, DetailView):
    model = models.Carro
    context_object_name = 'carro'
    template_name = 'core/carro.html'


class EditarCarro(LoginRequiredMixin, UpdateView):
    model = models.Carro
    fields = '__all__'
    template_name = 'core/editar_carro.html'
    success_url = reverse_lazy('carros')


class RemoverCarro(LoginRequiredMixin, DeleteView):
    model = models.Carro
    context_object_name = 'carro'
    template_name = 'core/remover_carro.html'
    success_url = reverse_lazy('carros')


# ########## CRUD MARCA CARRO ###########
class ListaMarcas(LoginRequiredMixin, ListView):
    model = models.MarcaCarro
    context_object_name = 'marcas'
    template_name = 'core/marcas.html'


class CadastrarMarca(LoginRequiredMixin, CreateView):
    model = models.MarcaCarro
    fields = '__all__'
    template_name = 'core/cadastrar_marca.html'
    success_url = reverse_lazy('marcas')

    def form_valid(self, form):
        return super(CadastrarMarca, self).form_valid(form)


class EditarMarca(LoginRequiredMixin, UpdateView):
    model = models.MarcaCarro
    fields = '__all__'
    template_name = 'core/editar_marca.html'
    success_url = reverse_lazy('marcas')


class RemoverMarca(LoginRequiredMixin, DeleteView):
    model = models.MarcaCarro
    context_object_name = 'marca'
    template_name = 'core/remover_marca.html'
    success_url = reverse_lazy('marcas')


# ########## CRUD ITEM = PEÇA/MATERIAL ###########
class ListaItens(LoginRequiredMixin, ListView):
    model = models.Item
    context_object_name = 'itens'
    template_name = 'core/itens.html'


class CadastrarItem(LoginRequiredMixin, CreateView):
    model = models.Item
    fields = '__all__'
    template_name = 'core/cadastrar_item.html'
    success_url = reverse_lazy('itens')

    def form_valid(self, form):
        return super(CadastrarItem, self).form_valid(form)


class EditarItem(LoginRequiredMixin, UpdateView):
    model = models.Item
    fields = '__all__'
    template_name = 'core/editar_item.html'
    success_url = reverse_lazy('itens')


class RemoverItem(LoginRequiredMixin, DeleteView):
    model = models.Item
    context_object_name = 'item'
    template_name = 'core/remover_item.html'
    success_url = reverse_lazy('itens')



# ########## CRUD CLIENTE ###########
class ListaClientes(LoginRequiredMixin, ListView):
    model = models.Cliente
    context_object_name = 'clientes'
    template_name = 'core/clientes.html'


class CadastrarCliente(LoginRequiredMixin, CreateView):
    model = models.Cliente
    fields = '__all__'
    template_name = 'core/cadastrar_cliente.html'
    success_url = reverse_lazy('clientes')

    def form_valid(self, form):
        return super(CadastrarCliente, self).form_valid(form)

class VerCliente(LoginRequiredMixin, DetailView):
    model = models.Cliente
    context_object_name = 'cliente'
    template_name = 'core/cliente.html'


class EditarCliente(LoginRequiredMixin, UpdateView):
    model = models.Cliente
    fields = '__all__'
    template_name = 'core/editar_cliente.html'
    success_url = reverse_lazy('clientes')


class RemoverCliente(LoginRequiredMixin, DeleteView):
    model = models.Cliente
    context_object_name = 'cliente'
    template_name = 'core/remover_cliente.html'
    success_url = reverse_lazy('clientes')

# ########## ORDEM DE SERVICO ###########
class ListaOs(LoginRequiredMixin, ListView):
    model = models.OrdemServico
    context_object_name = 'oss'
    template_name = 'core/oss.html'

class CadastrarOs(LoginRequiredMixin, CreateView):
    model = models.OrdemServico
    fields = '__all__'
    template_name = 'core/cadastrar_os.html'
    success_url = reverse_lazy('oss')

    def form_valid(self, form):
        return super(CadastrarOs, self).form_valid(form)

class EditarOs(LoginRequiredMixin, UpdateView):
    model = models.OrdemServico
    fields = '__all__'
    template_name = 'core/editar_os.html'
    success_url = reverse_lazy('oss')