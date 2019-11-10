from django.db import models

# Create your models here.
class Funcionarios(models.Model):
    Nome = models.CharField(max_length=90, help_text='Nome do Funcionario')



