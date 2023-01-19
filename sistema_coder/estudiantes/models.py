from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.comision}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)
    

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Medico(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    matricula = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)
    bio = models.TextField(null=True)
    especialidad = models.CharField(blank=True, max_length=32)
    comision = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

        
class Instituto(models.Model):
    nombre = models.CharField(max_length=256)
