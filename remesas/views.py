from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def remesas(request):
    usuarios= Member.objects.all().values()
    template =loader.get_template('clientes.html')
    context={
        'usuarios': usuarios,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    usuarios = Member.objects.get(id=id)
    template = loader.get_template('detail.html')
    context={
        'usuarios': usuarios,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template =loader.get_template("main.html")
    return HttpResponse(template.render())

def Datos(request):
    mydata= Member.objects.values_list('orden')
    template =loader.get_template('datos.html')
    context={
        'usuarios': mydata,
    }
    return HttpResponse(template.render(context,request))
#Crear aquí las vistas.