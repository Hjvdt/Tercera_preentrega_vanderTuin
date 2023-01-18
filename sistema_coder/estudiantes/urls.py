from django.urls import path

from estudiantes.views import  *

from estudiantes.views import (
    listar_estudiantes, listar_profesor, listar_cursos, 
    crear_curso, buscar_cursos, ver_curso, editar_curso, eliminar_curso, ver_profesor, 
    EstudianteListView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView,
    EstudianteDetailView

)
 
urlpatterns = [
    path('profesor/', listar_profesor, name="listar_profesor"),
    path('crear-profesor/', crear_profesor, name="crear_profesor"),
    path('buscar-profesor/', buscar_profesor, name="buscar_profesor"),
    path('profesor/', ver_profesor, name="ver_profesor"),
    path('editar-profesor/<int:id>/', editar_profesor, name="editar_profesor"),
    path('eliminar-profesor/<int:id>/', eliminar_profesor, name="eliminar_profesor"),
    # URLS de cursos (basadas den views funcionales)
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path('cursos/<int:id>/', ver_curso, name="ver_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    # URLS de alumnos (basadas den Class Based Views, vistas basadas en clases)
    path('alumnos/', EstudianteListView.as_view(), name="listar_alumnos"),
    path('alumnos/', EstudianteListView.as_view(), name="listar_estudiantes"),
    path('alumnos/<int:pk>/', EstudianteDetailView.as_view(), name="ver_alumno"),
    path('alumnos/<int:pk>/', EstudianteDetailView.as_view(), name="ver_estudiante"),
    path('crear-alumno/', EstudianteCreateView.as_view(), name="crear_alumno"),
    path('crear-alumno/', EstudianteCreateView.as_view(), name="crear_estudiante"),
    path('editar-alumno/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_alumno"),
    path('editar-alumno/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path('eliminar-alumno/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_alumno"),
    path('eliminar-alumno/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_estudiante"),
]
