from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from estudiantes.models import Paciente, Medico, Especialidad
from estudiantes.forms import EspecialidadFormulario, PacienteFormulario, MedicoFormulario
 

def inicio(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )

# ver, editar, borrar y listar Pacientes
def listar_pacientes(request):
    contexto = {
        'paciente': Paciente.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_pacientes.html',
        context=contexto,
    )


def crear_paciente(request):
    if request.method == "POST":
        formulario = PacienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            paciente = Paciente(nombre=data['nombre'], comision=data['comision'])
            paciente.save()
            url_exitosa = reverse('listar_paciente')
            return redirect(url_exitosa)
    else:  # GET
        formulario = PacienteFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_paciente.html',
        context={'formulario': formulario},
    )


def buscar_paciente(request):          
    if request.method == "POST":
        data = request.POST
        paciente = Paciente.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(apellido__exact=data['busqueda'])
        )
        contexto = {
            'paciente': paciente
        }
        return render(
            request=request,
            template_name='estudiantes/lista_paciente.html',
            context=contexto,
        )

def ver_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    contexto = {
        'paciente': paciente
    }
    return render(
        request=request,
        template_name='estudiantes/detalle_paciente.html',
        context=contexto,
    )

def buscar_paciente(request):
    if request.method == "POST":
        data = request.POST
        paciente = Paciente.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(apellido__exact=data['busqueda'])
        )
        contexto = {
            'paciente': paciente
        }
        return render(
            request=request,
            template_name='estudiantes/lista_pacientes.html',
            context=contexto,
        )

def editar_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == "POST":
        formulario = PacienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            paciente.nombre = data['nombre']
            paciente.apellido = data['apellido']
            paciente.especialidad = data['especialidad']
            paciente.comision = data['comision']
            paciente.save()
            url_exitosa = reverse('listar_paciente')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': paciente.nombre,
            'apellido': paciente.apellido,
            'especialidad': paciente.especialidad,
            'comision': paciente.comision,
        }
        formulario = PacienteFormulario(initial=inicial)
    return render(
        request=request,
        template_name='estudiantes/formulario_paciente.html',
        context={'formulario': formulario, 'paciente': paciente, 'es_update': True},
    )

def eliminar_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == "POST":
        paciente.delete()
        url_exitosa = reverse('listar_paciente')
        return redirect(url_exitosa)


# ver, editar, borrar y listar Medico

def listar_medico(request):
    contexto = {
        'medico': Medico.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_medico.html',
        context=contexto,
    )

def ver_medico(request, id):
    medico = Medico.objects.get(id=id)
    contexto = {
        'medico': medico
    }
    return render(
        request=request,
        template_name='estudiantes/detalle_medico.html',
        context=contexto,
    )

def crear_medico(request):
    
    if request.method == "POST":
        formulario = MedicoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            medico = Medico(
                nombre=data['nombre'], apellido=data['apellido'], especialidad=data['especialidad'], matricula=data['matricula'], email=data['email'])
            medico.save()
            url_exitosa = reverse('listar_medico')
            return redirect(url_exitosa)
    else:  # GET
        formulario = MedicoFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_medico.html',
        context={'formulario': formulario},
    )


def buscar_medico(request):
    if request.method == "POST":
        data = request.POST
        medico = Medico.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(apellido__exact=data['busqueda'])
        )
        contexto = {
            'medico': medico
        }
        return render(
            request=request,
            template_name='estudiantes/lista_medico.html',
            context=contexto,
        )

def editar_medico(request, id):
    medico = Medico.objects.get(id=id)
    if request.method == "POST":
        formulario = MedicoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            medico.nombre = data['nombre']
            medico.apellido = data['apellido']
            medico.especialidad = data['especialidad']
            medico.comision = data['comision']
            medico.save()
            url_exitosa = reverse('listar_medico')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': medico.nombre,
            'apellido': medico.apellido,
            'especialidad': medico.especialidad,
            'comision': medico.comision,
        }
        formulario = MedicoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='estudiantes/formulario_medico.html',
        context={'formulario': formulario, 'medico': medico, 'es_update': True},
    )

def eliminar_medico(request, id):
    medico = Medico.objects.get(id=id)
    if request.method == "POST":
        medico.delete()
        url_exitosa = reverse('listar_medico')
        return redirect(url_exitosa)


# ver, editar, borrar y listar especialidades
def listar_especialidades(request):
    contexto = {
        'especialidades': Especialidad.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_especialidades.html',
        context=contexto,
    )

def ver_especialidad(request, id):
    especialidad = Especialidad.objects.get(id=id)
    contexto = {
        'especialidad': especialidad
    }
    return render(
        request=request,
        template_name='estudiantes/detalle_especialidad.html',
        context=contexto,
    )


def crear_especialidad(request):
    if request.method == "POST":
        formulario = EspecialidadFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            especialidad = Especialidad(nombre=data['nombre'], comision=data['comision'], descripcion = data['descripcion'])
            especialidad.save()
            url_exitosa = reverse('listar_especialidades')
            return redirect(url_exitosa)
    else:  # GET
        formulario = EspecialidadFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_especialidad.html',
        context={'formulario': formulario},
    )


def buscar_especialidades(request):
    if request.method == "POST":
        data = request.POST
        especialidades = Especialidad.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__contains=data['busqueda'])
        )
        contexto = {
            'especialidades': especialidades
        }
        return render(
            request=request,
            template_name='estudiantes/lista_especialidades.html',
            context=contexto,
        )


def editar_especialidad(request, id):
    especialidad = Especialidad.objects.get(id=id)
    if request.method == "POST":
        formulario = EspecialidadFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            especialidad.nombre = data['nombre']
            especialidad.comision = data['comision']
            especialidad.descripcion = data['descripcion']
            especialidad.save()
            url_exitosa = reverse('listar_especialidades')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': especialidad.nombre,
            'comision': especialidad.comision,
            'descripcion': especialidad.descripcion,
        }
        formulario = EspecialidadFormulario(initial=inicial)
    return render(
        request=request,
        template_name='estudiantes/formulario_especialidad.html',
        context={'formulario': formulario, 'especialidad': especialidad, 'es_update': True},
    )

def eliminar_especialidad(request, id):
    especialidad = Especialidad.objects.get(id=id)
    if request.method == "POST":
        especialidad.delete()
        url_exitosa = reverse('listar_especialidades')
        return redirect(url_exitosa)



class PacienteListView(ListView):
    model = Paciente
    template_name = 'estudiantes/lista_pacientes.html'


class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_pacientes')


class PacienteDetailView(DetailView):
    model = Paciente
    success_url = reverse_lazy('listar_pacientes')


class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_pacientes')


class PacienteDeleteView(DeleteView):
    model = Paciente
    success_url = reverse_lazy('listar_pacientes')






