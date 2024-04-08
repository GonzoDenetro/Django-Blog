from django import forms
from django.forms import ModelForm #ModelForm nos permite relacionar un formulario con un modelo
from django.forms import Form
from .models import Post


class PostForm(ModelForm): #Heredamos de ModelForm
    class Meta():
        model = Post
        fields = ['titutlo', 'contenido'] #Los campos del formulario son los campos del modelo


class ContactForm(Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.CharField(required=True, widget=forms.EmailInput())
    asunto = forms.CharField(required=True, widget=forms.TimeInput())
    mensaje = forms.CharField(required=True, widget=forms.Textarea())