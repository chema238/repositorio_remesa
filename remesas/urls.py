from django.urls import path
from . import views

urlpatterns = [
    path('remesas/', views.remesas, name='remesas'),
    #path('remesas/Datos_de_Remesa/<int:Orden>', views.Datos_de_Remesa, name='Datos_de_Remesa'),
]
