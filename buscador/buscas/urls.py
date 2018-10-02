from django.conf.urls import url
from django.contrib import admin
from buscas import views
from buscas.views import RegistrarBuscaView

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^buscar/', RegistrarBuscaView.as_view(), name='buscar'),
]
