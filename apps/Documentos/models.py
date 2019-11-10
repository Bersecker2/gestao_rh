from django.db import models
from apps.Funcionarios.models import Funcionarios

class Documentos(models.Model):
    Nome = models.CharField(max_length=70, help_text="Nome do documento")
    Funcionarios = models.ForeignKey(Funcionarios, on_delete=models.SET_NULL, null=True)