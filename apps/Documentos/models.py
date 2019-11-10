from django.db import models

class Documentos(models.Model):
    Nome = models.CharField(max_length=70, help_text="Nome do documento")
