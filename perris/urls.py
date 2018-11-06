from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index),
    url(r'^principal/', views.principal, name = 'principal'),
    url(r'^registro/', 	views.registro, name = 'registro'),
    url(r'^login/', views.login, name = 'login'),
    url(r'^administracion/', views.administracion, name='administracion'),
    url(r'^agregarMascota/', views.agregarMascota, name='agregarMascota'),
    url(r'^listaRescatado/', views.ListaRescatado.as_view(), name ='listaRescatado'),
    url(r'^editar/(?P<pk>\d+)/', views.RescatadoUpdate.as_view(), name ='editarRescatado'),
    url(r'^eliminar/(?P<pk>\d+)/', views.RescatadoDelete.as_view(), name ='eliminarRescatado')

]
