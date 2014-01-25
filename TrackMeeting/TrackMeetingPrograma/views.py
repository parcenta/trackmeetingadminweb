from TrackMeetingPrograma.models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.core import serializers
from django.http.response import HttpResponse

def lista_empleados(request):
    empleado = Empleado.objects.all()
    return ('empleados.html',{'listaEmpleados':empleado})

def pantalla_inicio(request):
    return render_to_response('inicio.html')






# XML Responses para Android
def empleados_xml(request):
    return render_to_response("empleados.xml", {'listaEmpleados':Empleado.objects.all()} , content_type="application/xhtml+xml")
# XML Responses para Android
def reunionesProximas_xml(request):
    return render_to_response("reuniones.xml", {'listaReuniones':Reunion.objects.order_by('fecha')} , content_type="application/xhtml+xml")