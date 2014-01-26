from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackMeeting.views.home', name='home'),
    # url(r'^TrackMeeting/', include('TrackMeeting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^empleados/','TrackMeetingPrograma.views.lista_empleados'),
    
    url(r'^$','TrackMeetingPrograma.views.pantalla_inicio'),
    
    # XMLs para Android
    url(r'^empleadosXML/','TrackMeetingPrograma.views.empleados_xml'),
    url(r'^proximasReunionesXML/(?P<idempleado>\d+)$','TrackMeetingPrograma.views.reunionesProximas_de_un_Empleado_xml'),
)
