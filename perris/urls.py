from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index),
    url(r'^principal/', TemplateView.as_view(template_name="perris/Principal.html"),
    					name='principal'),
    url(r'^registro/', TemplateView.as_view(template_name="perris/Registro.html"),
    					name='registro'),

]
