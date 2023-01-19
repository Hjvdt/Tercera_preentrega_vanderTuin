from django.apps import AppConfig


class PacienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pacientes'

class MedicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medico'

class ComisionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comision'

class EspecialidadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'especialidad'