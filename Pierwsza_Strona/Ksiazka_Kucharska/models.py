from django.db import models

class Typ_nadwozia(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
      
class Samochod(models.Model):
    name = models.CharField(max_length=200, null=True)
    opis = models.CharField(max_length=600, null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True) 
    typ = models.ManyToManyField("Typ_nadwozia")

    def __str__(self):
        return self.name
   



