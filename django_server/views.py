from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
def saludos(request):
    nombre='kenny'
    #doc_externo = open('C:/Users/kjmol/Documents/CODES/meProjects/django-server/django_server/django_server/plantillas/hola.html')
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    # explicacion de donde se carga esto en el readme usando dirs en settings.py
    doc_externo = loader.get_template('hola.html')
    ctx=Context({"nombre":nombre,"apellido":"molina","temas":["tema1","tema2","tema3"]})
    documento=doc_externo.render({"nombre":nombre,"apellido":"molina","temas":["tema1","tema2","tema3"]})
    return HttpResponse(documento)
def edad (request, anio ):
    return HttpResponse(anio)