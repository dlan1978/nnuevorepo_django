from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso, Profesor, Alumno
from django.template import loader 
from app_coder.forms import Curso_formulario, Profesor_formulario, Alumno_formulario

# Create your views here.

def inicio(request):

    return render( request , "plantillas.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def alta_curso(request, nombre):
    curso =Curso(nombre=nombre , camada=287318)
    curso.save()
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)

def alumnos(request):

    return render( request , "alumnos.html")

def contacto(request):
    
    return render( request , "contacto.html")

def profesores(request):
    
    return render( request , "profesores.html")

#ALTA CURSO
def curso_formulario(request):
    
    if request.method == "POST":
        
        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
        
            curso = Curso( nombre=request.POST['nombre'] , camada=request.POST['camada']) 
            curso.save()
        
        
        return render( request , "formulario.html")

    return render( request , "formulario.html")




#ALTA PROFESORES
def alta_profesores(request):
    
    if request.method == "POST":
        
        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
        
            profesor = Profesor( nombre=request.POST['nombre'] , legajo=request.POST['legajo']) 
            profesor.save()
        
        
        return render( request , "formulario.html")

    return render( request , "alta_profesores.html")

#ALTA ALUMNOS
def alta_alumnos(request):
    
    if request.method == "POST":
        
        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
        
            alumno = Alumno( nombre=request.POST['nombre'] , camada=request.POST['camada']) 
            alumno.save()
        
        
        return render( request , "formulario.html")

    return render( request , "alta_alumnos.html")


def buscar_curso(request):
    
    return render( request , "buscar_curso.html")


def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
    
