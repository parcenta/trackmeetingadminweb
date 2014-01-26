from TrackMeetingPrograma.models import *
from TrackMeetingPrograma.forms import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def lista_empleados(request):
    empleado = Empleado.objects.all()
    return render_to_response('empleados.html', {'listaEmpleados' : empleado},context_instance=RequestContext(request))

def pantalla_inicio(request):
    proximasreuniones = Reunion.objects.order_by('fecha','hora')
    formulario = ReunionForm()
    return render_to_response('inicio.html',{'listaProximasReuniones' : proximasreuniones , 'formulario':formulario} , context_instance=RequestContext(request))
    


#Formularios
#def save_Reunion
#    if request.method == 'POST':
#        formulario= ReunionForm(request.POST,request.FILES)
#        if formulario.is_valid():
#            formulario.save()
#            return HttpResponseRedirect('/inicio')
#    else:


# XML Responses para Android
def empleados_xml(request):
    return render_to_response("empleados.xml", {'listaEmpleados':Empleado.objects.all()} , content_type="application/xhtml+xml")
# XML Responses para Android

def reunionesProximas_xml(request):
    return render_to_response("reuniones.xml", {'listaReuniones':Reunion.objects.order_by('fecha','hora')} , content_type="application/xhtml+xml")

def reunionesProximas_de_un_Empleado_xml(request,idempleado):
    reuniones = Reunion.objects.filter(empleado_idempleado=idempleado).order_by('fecha','hora')
    return render_to_response("reuniones.xml", {'listaReuniones':reuniones} , content_type="application/xhtml+xml")