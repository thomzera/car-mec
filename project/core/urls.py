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
]
