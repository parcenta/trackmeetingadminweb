from django.forms import ModelForm
from django import forms
from models import Reunion,Cliente


class ReunionForm(ModelForm):
    class Meta:
        model = Reunion
        fields = ['cliente_id_cliente','empleado_idempleado','motivo','descripcion','direccion','fecha','hora']
        
class Reunion(Cliente):
    def __unicode__(self):
        return self.nombre 