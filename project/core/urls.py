from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # LOGIN LOGOUT REGISTER
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("registrar/", views.RegistroUsuario.as_view(), name="registrar"),

    # CRUD CARROS
    path("carros/", views.ListaCarros.as_view(), name="carros"),
    path("carros/cadastrar/",
         views.CadastrarCarro.as_view(), name="cadastrar_carro"),
    path("carros/ver/<int:pk>/", views.VerCarro.as_view(), name="ver_carro"),
    path("carros/editar/<int:pk>/",
         views.EditarCarro.as_view(), name="editar_carro"),
    path("carros/remover/<int:pk>/",
         views.RemoverCarro.as_view(), name="remover_carro"),


    # CRUD MARCAS DE CARROS
    path("marcas/", views.ListaMarcas.as_view(), name="marcas"),
    path("marcas/cadastrar/",
         views.CadastrarMarca.as_view(), name="cadastrar_marca"),
    path("marcas/editar/<int:pk>/",
         views.EditarMarca.as_view(), name="editar_marca"),
    path("marcas/remover/<int:pk>/",
         views.RemoverMarca.as_view(), name="remover_marca"),


     # CRUD ITENS
    path("itens/", views.ListaItens.as_view(), name="itens"),
    path("itens/cadastrar/",
         views.CadastrarItem.as_view(), name="cadastrar_item"),
    path("itens/editar/<int:pk>/",
         views.EditarItem.as_view(), name="editar_item"),
    path("itens/remover/<int:pk>/",
         views.RemoverItem.as_view(), name="remover_item"),


     # CRUD CLIENTES
    path("clientes/", views.ListaClientes.as_view(), name="clientes"),
    path("clientes/cadastrar/",
         views.CadastrarCliente.as_view(), name="cadastrar_cliente"),
     path("clientes/ver/<int:pk>/", views.VerCliente.as_view(), name="ver_cliente"),
    path("clientes/editar/<int:pk>/",
         views.EditarCliente.as_view(), name="editar_cliente"),
    path("clientes/remover/<int:pk>/",
         views.RemoverCliente.as_view(), name="remover_cliente"),


     # ORDEM SERVICO
     path("os/", views.ListaOs.as_view(), name="oss"),
     path("os/cadastrar/",
         views.CadastrarOs.as_view(), name="cadastrar_os"),
     path("os/editar/<int:pk>/",
         views.EditarOs.as_view(), name="editar_os"),

     # FINANCEIRO
     path("financeiro/", views.Financeiro.as_view(), name="financeiro")
]
