from django.db import models

# Create your models here.


class Departamentos(models.Model):
    Nome = models.CharField(max_length=70, help_text="Nome do Departamento")




