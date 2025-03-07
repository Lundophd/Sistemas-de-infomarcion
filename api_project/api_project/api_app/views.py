from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics , status
from django.db.models import Q
from rest_framework import filters
from rest_framework.exceptions import NotFound, ValidationError
from .models import Autor, Editorial, Libro,Miembro,Prestamo
from .serializers import AutorSerializer,MiembroSerializer,EditorialSerializer, LibroSerializer,PrestamoSerializer

class AutorListCreate(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get(self, request):
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        if not autores:
            raise NotFound('No se encontraron Autores')
        return Response({'success': True, 'detail': 'Listado de Autores.', 'data': serializer.data}, status=status.HTTP_200_OK)


class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def post(self, request):
        serializer = AutorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Autor creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)


class EditorialListCreate(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class EditorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroListCreate(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_queryset(self):
        queryset = Libro.objects.all()
        autor = self.request.query_params.get('autor')
        editorial = self.request.query_params.get('editorial')
        if autor:
            queryset = queryset.filter(autor__id=autor)
        if editorial:
            queryset = queryset.filter(editorial__id=editorial)
        return queryset

class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class MiembroListCreate(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

class MiembroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

class PrestamoListCreate(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get_queryset(self):
        queryset = Prestamo.objects.all()
        miembro = self.request.query_params.get('miembro')
        fecha_prestamo = self.request.query_params.get('fecha_prestamo')
        if miembro:
            queryset = queryset.filter(miembro__id=miembro)
        if fecha_prestamo:
            queryset = queryset.filter(fecha_prestamo=fecha_prestamo)
        return queryset

class PrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer


