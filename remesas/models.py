from django.db import models

class Member(models.Model):
  Usuario = models.CharField(max_length=255)
  Orden = models.CharField(max_length=255)
  

def __str__(self):
  return f"{self.Usuario} {self.Orden}"

class Operacion(models.Model):
  Phone= models.IntegerField(9)
  Firstname= models.CharField(max_length=100)
  Lastname= models.CharField(max_length=50)
  Cantidad= models.FloatField(max_length=100)
  IBAN= models.CharField(max_length=24)
  Beneficiario=models.CharField(max_length=100)
  Concepto= models.CharField(max_length=100)
  Bank= models.CharField(max_length= 100)
  BIC: models.CharField(max_length=50)

  def __str__(self):
      return f"{self.Phone}{self.Firstname}{self.Lastname}{self.Cantidad}{self.IBAN}{self.Beneficiario}{self.Concepto}{self.Bank}{self.BIC}"
  

# Create your models here.


