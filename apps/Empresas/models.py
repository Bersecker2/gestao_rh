from django.db import models

#Representa entidade empresa do banco de dados
class Empresa(models.Model):
    Nome = models.CharField(max_length=70, help_text='Nome da Empresa')









