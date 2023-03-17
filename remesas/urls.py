from django.urls import path
from . import views

urlpatterns = [
   path('', views.main, name= 'main'),
   path('remesas/', views.remesas, name='remesas'),
   path('remesas/details/', views.details, name='details'),
   path('Datos/',views.Datos, name='Datos'),
]
