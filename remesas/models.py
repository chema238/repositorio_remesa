from django.db import models

class Member(models.Model):
  Usuario = models.CharField(max_length=255)
  Orden = models.CharField(max_length=255)
  

def __str__(self):
  return f"{self.Usuario} {self.Orden}"
# Create your models here.


