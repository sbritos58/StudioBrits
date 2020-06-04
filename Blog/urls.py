from django.urls import path,include
from .views import *
urlpatterns = [
    path("Blog/Crear/<slug:hola>",CrearPost.as_view(), name = "CrearPost"),
    path("Blog/Editar/<int:pk>/<slug:hola>",ActualizarPosts.as_view(), name = "ActualizarPost"),
    path("Blog/Crear/<int:pk>/<slug:hola>",BorrarPost.as_view(), name = "BorrarPost"),
    path("Blog/Detalle/<int:pk>/<slug:hola>",DetallePost.as_view(), name = "DetallePost"),
    path("Blog/Listar",ListarPost.as_view(), name = "ListarPosts"),

    #Crear Categoria

    path("Categorias/Crear/<slug:hola>",CrearCategoria.as_view(), name = "CrearCategorias"),
]