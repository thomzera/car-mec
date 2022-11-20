from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),

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
