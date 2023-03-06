from django.http import HttpResponse
from django.template import loader
from .models import Member

def remesas(request):
    myusuarios=Member.objects.all().values()
    template = loader.get_template('Datos_de_Remesa.html')
    context={
        "myusuarios": myusuarios,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.
def presentacion(request, Orden):
  myusuarios = Member.objects.get(Orden=Orden)
  template = loader.get_template('Datos_de_Remesa.html')
  context = {
    'myusuarios': myusuarios,
  }
  return HttpResponse(template.render(context, request))