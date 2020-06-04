import email

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, ListView, UpdateView, DetailView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


from Blog.forms import FormPost, FormCategoria, FormContactForm
from Blog.models import Post, Categorias


class BorrarPost(DeleteView):
    model = Post
    success_url = reverse_lazy('ListarPosts')
    template_name = "blog/borrar.html"

    def get_success_url(self):
        success_message = '¡¡¡ Post eliminado correctamente !!!'
        messages.success(self.request, (success_message))
        return reverse_lazy('ListarPosts')


class CrearPost(SuccessMessageMixin, CreateView):
    template_name = "blog/crear.html"
    form_class = FormPost
    success_message = '¡¡ Post creado correctamente !!'

    def get_success_url(self):
        return reverse_lazy('ListarPosts')


class ListarPost(ListView):
    template_name = "blog/listar.html"
    model = Post


class ActualizarPosts(UpdateView):
    success_message = '¡¡ Post actualizado correctamente !!'
    model = Post
    template_name = "blog/editar.html"
    fields = ["titulo", "contenido", "imagen","publicado","autor","categorias"]

    def get_success_url(self):
        return reverse_lazy('ListarPosts')


class DetallePost(DetailView):
    model = Post
    template_name = "blog/detalle.html"


class CrearCategoria(SuccessMessageMixin, CreateView):
    template_name = "blog/crearCategoria.html"
    form_class = FormCategoria
    success_message = '¡¡ Categoría creada correctamente !!'

    def get_success_url(self):
        return reverse_lazy('ListarPosts')


class CrearFormularioContacto(CreateView):
    form_class = FormContactForm
    template_name = "base.html"
    success_message = '¡¡ Formulario enviado correctamente !!'

    def get_success_url(self):
        return reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            form = self.get_form()
            if form.is_valid():
                data["nombre_completo"] = request.POST["nombre_completo"]
                data["descripcion"] = request.POST["descripcion"]
                data["email"] = request.POST["email"]

                body = render_to_string(
                    'email_content_cliente.html',{
                        "nombre":request.POST["nombre_completo"],
                        "descripcion": request.POST["descripcion"],
                        "email": request.POST["email"],
                    },
                )

                email_message = EmailMessage(
                    subject='Consulta realizada correctamente',
                    body=body,
                    from_email=email,
                    to=[request.POST["email"],"info@StudioBrits.com"],

                )
                email_message.content_subtype = 'html'
                email_message.send()
                form.save()
            else:
                data = form.errors
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)
