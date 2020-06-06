from django.urls import path,include
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("Blog/Crear/<slug:hola>",login_required(CrearPost.as_view()), name = "CrearPost"),
    path("Blog/Editar/<int:pk>/<slug:hola>",login_required(ActualizarPosts.as_view()), name = "ActualizarPost"),
    path("Blog/Crear/<int:pk>/<slug:hola>",login_required(BorrarPost.as_view()), name = "BorrarPost"),
    path("Blog/Detalle/<int:pk>/<slug:hola>",DetallePost.as_view(), name = "DetallePost"),
    path("Blog/Listar",ListarPost.as_view(), name = "ListarPosts"),

    #Crear Categoria

    path("Categorias/Crear/<slug:hola>",login_required(CrearCategoria.as_view()), name = "CrearCategorias"),
]