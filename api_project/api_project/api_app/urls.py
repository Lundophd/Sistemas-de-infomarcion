# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    PersonaList#, PersonaByDocumento, ActualizarPersona,
    #TareaList, TareaByFecha, TareaByRangoFechas, TareaByPersona
)

# Define la lista de patrones de URL para la aplicación 'api_app'
urlpatterns = [
    # Rutas para la gestión de personas
    # Lista de personas
    path('personas/', PersonaList.as_view(), name='persona-list'),
    # Crear una nueva persona
    path('personas/crear/', PersonaList.as_view(), name='persona-crear'),
]