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

    def get(self, request):
        editoriales = Editorial.objects.all()
        serializer = EditorialSerializer(editoriales, many=True)
        if not editoriales:
            raise NotFound('No se encontraron editoriales')
        return Response({'success': True, 'detail': 'Listado de editoriales.', 'data': serializer.data}, status=status.HTTP_200_OK)

class EditorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def post(self, request):
        serializer = EditorialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Editorial creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)

class LibroListCreate(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_queryset(self):
        queryset = Libro.objects.all()
        autor = self.request.query_params.get('autor')
        editorial = self.request.query_params.get('editorial')

        if autor:
            queryset = queryset.filter(autor_id=autor)
        if editorial:
            queryset = queryset.filter(editorial_id=editorial)

        if not queryset.exists():
            raise NotFound('No se encontraron libros')

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = LibroSerializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Listado de libros.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'libro creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)

class MiembroListCreate(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def get(self, request):
        miembros = Miembro.objects.all()
        serializer = MiembroSerializer(miembros, many=True)
        if not miembros:
            raise NotFound('No se encontraron Miembros')
        return Response({'success': True, 'detail': 'Listado de Miembros.', 'data': serializer.data}, status=status.HTTP_200_OK)

class MiembroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def post(self, request):
        serializer = MiembroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'miembro creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)

class PrestamoListCreate(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get_queryset(self):
        queryset = Prestamo.objects.all()
        miembro = self.request.query_params.get('miembro')
        fecha_prestamo = self.request.query_params.get('fecha_prestamo')
        if miembro:
            queryset = queryset.filter(miembro_id=miembro)
        if fecha_prestamo:
            queryset = queryset.filter(fecha_prestamo=fecha_prestamo)
        prestamos = Prestamo.objects.all()
        serializer = PrestamoSerializer(prestamos, many=True)
        if not prestamos:
            raise NotFound('No se encontraron prestamos')
        Response({'success': True, 'detail': 'Listado de prestamos.', 'data': serializer.data}, status=status.HTTP_200_OK)

        return queryset

class PrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def post(self, request):
        serializer = PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'prestamo creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
