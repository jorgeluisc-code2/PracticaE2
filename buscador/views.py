from django.shortcuts import render
from rest_framework import generics, filters, status
from buscador.models import Institucion
from buscador.serializers import InstitutoSerializer


class InstitutoAPIView(generics.ListCreateAPIView):
    search_fields = ['tipoInstitucion']
    filter_backends = (filters.SearchFilter,)
    queryset = Institucion.objects.all()
    serializer_class = InstitutoSerializer

class InstitutoRUCAPIView2(generics.ListCreateAPIView):
    search_fields = ['ruc']
    filter_backends = (filters.SearchFilter,)
    queryset = Institucion.objects.all()
    serializer_class = InstitutoSerializer

