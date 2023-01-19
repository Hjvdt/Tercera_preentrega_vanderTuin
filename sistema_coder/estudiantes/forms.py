from django import forms


class EspecialidadFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)
    descripcion = forms.CharField(max_length=64)

class MedicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    apellido = forms.CharField(max_length=64)
    matricula = forms.CharField(max_length=32)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    bio = forms.CharField(max_length=256)
    especialidad = forms.CharField(max_length=64)
    comision = forms.IntegerField()
    

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    apellido = forms.CharField(max_length=64)
    