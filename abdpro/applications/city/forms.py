# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import City

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NewCityForm(forms.ModelForm):
    """Form definition for Empleado."""
    class Meta:
        """Meta definition for Empleadoform."""
        # Modelo al que se aplica el formulario
        model = City
        # Campos usados en el formulario
        fields = (
            'name',
            'idcountry',
            'district',
            'population',
        )
        # Labels de los campos del formulario
        labels = {
            'name': 'Name of city',
            'idcountry': 'id Country',
            'district': 'District',
            'population': 'population',
        }
                # Espacio para agregar características a los campos
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'ContainerCityFormSelect'}
            ),
        }