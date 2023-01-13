from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from estudiantes.models import Estudiante, Profesor, Curso
from estudiantes.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
 

def inicio(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )


def listar_estudiantes(request):
    ## Aqui iria la validacion del permiso lectura estudiantes
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto,
    )


def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesores.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_cursos.html',
        context=contexto,
    )


def crear_curso_version_1(request):
    """No la estamos usando"""
    if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], comision=data['comision'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:  # GET
        return render(
            request=request,
            template_name='estudiantes/formulario_curso_a_mano.html',
        )


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], comision=data['comision'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_curso.html',
        context={'formulario': formulario},
    )


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )

def crear_profesor(request):
    if request.method == "POST":
        formulario =ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], curso=data['curso'], comision=data['comision'])
            profesor.save()
            url_exitosa = reverse('listar_profesor')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_profesor.html',
        context={'formulario': formulario},
    )


def buscar_profesor(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )

def crear_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante = Estudiante(nombre=data['nombre'], comision=data['comision'])
            estudiante.save()
            url_exitosa = reverse('listar_estudiante')
            return redirect(url_exitosa)
    else:  # GET
        formulario = EstudianteFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_estudiante.html',
        context={'formulario': formulario},
    )


def buscar_estudiante(request):          
    if request.method == "POST":
        data = request.POST
        estudiante = Estudiante.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'estudiante': estudiante
        }
        return render(
            request=request,
            template_name='estudiantes/lista_estudiante.html',
            context=contexto,
        )

