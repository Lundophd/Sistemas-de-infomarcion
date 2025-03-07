# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import *#, PersonaByDocumento, ActualizarPersona,
    #TareaList, TareaByFecha, TareaByRangoFechas, TareaByPersona


# Define la lista de patrones de URL para la aplicación 'api_app'
urlpatterns = [
    # Rutas para la gestión de personas
    # Lista de personas

    path('autores/', AutorListCreate.as_view(), name='autor-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),
    
    path('editoriales/', EditorialListCreate.as_view(), name='editorial-list'),
    path('editoriales/<int:pk>/', EditorialDetail.as_view(), name='editorial-detail'),
    
    path('libros/', LibroListCreate.as_view(), name='libro-list'),
    path('libros/<int:pk>/', LibroDetail.as_view(), name='libro-detail'),
    
    path('miembros/', MiembroListCreate.as_view(), name='miembro-list'),
    path('miembros/<int:pk>/', MiembroDetail.as_view(), name='miembro-detail'),
    
    path('prestamos/', PrestamoListCreate.as_view(), name='prestamo-list'),
    path('prestamos/<int:pk>/', PrestamoDetail.as_view(), name='prestamo-detail')
]