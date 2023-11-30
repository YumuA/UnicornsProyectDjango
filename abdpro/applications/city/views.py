from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

# ------------------------------------------------------------------
# APIS
# ------------------------------------------------------------------
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    # DetailView
    RetrieveAPIView,
    # Delete
    DestroyAPIView,
    # Actualizar
    UpdateAPIView,
    # Recupera y actualiza
    RetrieveUpdateAPIView,
    # Recupera y elimina
    RetrieveDestroyAPIView,
)

from .serializer import (
    CitySerializer
)
# ------------------------------------------------------------------
# VISTAS A USAR
# ------------------------------------------------------------------

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# ------------------------------------------------------------------
# MODELOS
# ------------------------------------------------------------------
from .models import City

# ------------------------------------------------------------------
# FORMULARIOS
# ------------------------------------------------------------------

from .forms import NewCityForm

# ------------------------------------------------------------------
# CREAR City
# ------------------------------------------------------------------

class NuevoCity(CreateView):
    # Modelo usado para la vista
    model = City
    # Template usado en la vista
    template_name = 'City/NuevoCity.html'
    # Contexto usado para la impresión en el html
    context_object_name = 'NewCity'
    # formulario usado en la vista
    form_class = NewCityForm
    # Dirección a la que va cuando se ejecuta el submit
    success_url = reverse_lazy('inicio_app:home')

    def form_valid(self, form):
        # Guardando los datos del formulario
        city = form.save(commit=False)
        city.save()
        # Return del formulario completado
        return super(NuevoCity, self).form_valid(form)

# ------------------------------------------------------------------
# API CREAR UN TRABAJO
# ------------------------------------------------------------------
#class TrabajoAPISerializer(CreateAPIView):
#   serializer_class = TrabajosSerializer

# ------------------------------------------------------------------
# API CREAR UN TRABAJO
# ------------------------------------------------------------------
class CityAPISerializer(CreateAPIView):
    serializer_class = CitySerializer