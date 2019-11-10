from django.db import models
from django.contrib.auth.models import User
from apps.Departamentos.models import Departamentos
from apps.Empresas.models import Empresa

class Funcionarios(models.Model):
    Nome = models.CharField(max_length=90, help_text='Nome do Funcionario')
    Usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    Departamentos = models.ManyToManyField(Departamentos)
    Empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

