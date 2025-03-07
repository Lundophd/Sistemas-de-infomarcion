from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics , status
from django.db.models import Q
from rest_framework.exceptions import NotFound, ValidationError
from .models import Persona, Tarea
from .serializers import PersonaSerializer, TareaSerializer

# Create your views here.
#listar
class PersonaList(generics.ListCreateAPIView):
    queryset= Persona.objects.all()
    serializer_class=PersonaSerializer

    def get(self,request):
        Personas= Persona.objects.all()
        serializer = PersonaSerializer(Personas, many=True)
        if not Personas:
            raise NotFound('No se encontraron Personas')
        return Response({'success':True, 'detail':'Listado de Personas.', 'data': serializer.data},status=status.HTTP_200_OK)
    
#crear
class CrearPersona(generics.CreateAPIView):
    queryset= Persona.objects.all()
    serializer_class=PersonaSerializer

    def post(self,request):
        serializer = PersonaSerializer(data = request.data)
        serializer.is_valid(raise_exeption = True)
        serializer.save()
        return Response({'seccess': True,'detail':'Persona creada correctamente.','data':serializer.data},status=status.HTTP_201_CREATED)
