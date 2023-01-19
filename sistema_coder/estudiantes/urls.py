from django.urls import path

from estudiantes.views import  *

from estudiantes.views import (
    listar_pacientes, listar_medico, listar_especialidades,
    crear_paciente, crear_medico, crear_especialidad, buscar_especialidades, buscar_medico, buscar_paciente,
    ver_especialidad, ver_medico, ver_paciente, editar_especialidad, editar_paciente, editar_medico, eliminar_especialidad, eliminar_medico, eliminar_paciente,
    PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView,
    PacienteDetailView

)
 
urlpatterns = [
    path('crear-medico/', crear_medico, name="crear_medico"),
    path('medico/', listar_medico, name="listar_medico"),
    path('buscar-medico/', buscar_medico, name="buscar_medico"),
    path('medicos/<int:id>/', ver_medico, name="ver_medico"),
    path('editar-medico/<int:id>/', editar_medico, name="editar_medico"),
    path('eliminar-medico/<int:id>/', eliminar_medico, name="eliminar_medico"),
    # URLS de especialidades (basadas den views funcionales)
    path('crear-especialidad/', crear_especialidad, name="crear_especialidad"),
    path('especialidades/', listar_especialidades, name="listar_especialidades"),
    path('buscar-especialidades/', buscar_especialidades, name="buscar_especialidades"),
    path('especialidades/<int:id>/', ver_especialidad, name="ver_especialidad"),
    path('editar-especialidad/<int:id>/', editar_especialidad, name="editar_especialidad"),
    path('eliminar-especialidad/<int:id>/', eliminar_especialidad, name="eliminar_especialidad"),
    # URLS de pacientes (basadas den Class Based Views, vistas basadas en clases)
    path('pacientes/', PacienteListView.as_view(), name="listar_pacientes"),
    path('buscar-paciente/', buscar_paciente, name="buscar_paciente"),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name="ver_paciente"),
    path('crear-paciente/', PacienteCreateView.as_view(), name="crear_paciente"),
    path('editar-paciente/<int:pk>/', PacienteUpdateView.as_view(), name="editar_paciente"),
    path('eliminar-paciente/<int:pk>/', PacienteDeleteView.as_view(), name="eliminar_paciente"),
]
