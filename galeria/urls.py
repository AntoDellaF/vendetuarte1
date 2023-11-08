from django.urls import path
from . import views

urlpatterns = [
    path('crear_cuadro/', views.crear_cuadro, name='crear_cuadro'),
    path('crear_escultura/', views.crear_escultura, name='crear_escultura'),
    path('crear_ceramica/', views.crear_ceramica, name='crear_ceramica'),
]
