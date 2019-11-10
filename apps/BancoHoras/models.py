from django.db import models

class BancoHoras(models.Model):
    Nome = models.CharField(max_length=70, help_text="Nome do Banco de horas")
