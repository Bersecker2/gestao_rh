from django.db import models
from apps.Funcionarios.models import Funcionarios

class BancoHoras(models.Model):
    Nome = models.CharField(max_length=70, help_text="Nome do Banco de horas")
    Funcionarios = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)