from django.forms import ModelForm
from .models import Categorias, Post, ContactForm


class FormPost(ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","contenido","autor","imagen","categorias"]

class FormCategoria(ModelForm):
    class Meta:
        model = Categorias
        fields = ["nombre"]

class FormContactForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ["nombre_completo","descripcion","email"]