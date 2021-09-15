from django.db import models

# Create your models here.

class Permissionario(models.Model):
    nome = models.CharField(max_length=40, verbose_name='Nome')
    cpf = models.CharField(max_length=40, verbose_name='CPF')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')

    def _str__(self):
        return f'Nome: {nome} | Telefone: {telefone}'


