from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index),
    url(r'^principal/', views.principal, name = 'principal'),
    url(r'^registro/', 	views.registro, name = 'registro'),

]
