from django.urls import path
from galeria.views import crear_cuadro, crear_escultura, crear_ceramica

urlpatterns = [
    path('crear_cuadro/', crear_cuadro, name='crear_cuadro'),
    path('crear_escultura/', crear_escultura, name='crear_escultura'),
    path('crear_ceramica/', crear_ceramica, name='crear_ceramica'),
]
