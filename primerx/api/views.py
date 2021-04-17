from django.shortcuts import render

from .models import primerx_field_model
from .serializers import PrimerxSerializer
from rest_framework.generics import ListAPIView

class primerxList(ListAPIView):
    queryset = primerx_field_model.objects.all()
    serializer_class = PrimerxSerializer
    