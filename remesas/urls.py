from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('remesas/', views.remesas, name='remesas'),
    path('operacion/',views.presentacion,name='operacion'),
]
