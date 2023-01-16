from django.apps import AppConfig


class EstudiantesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estudiantes'

class ProfesorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profesor'

class ComisionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comision'

class CursoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'curso'