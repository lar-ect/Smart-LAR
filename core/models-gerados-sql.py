# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.


class Acesso(models.Model):
    id_a = models.BigAutoField(primary_key=True)
    id_pes = models.ForeignKey('Pessoas', models.DO_NOTHING, db_column='id_pes')

    class Meta:
        # managed = False
        db_table = 'acesso'


class Admin(models.Model):
    id_admin = models.BigAutoField(primary_key=True)
    id_acesso = models.ForeignKey(Acesso, models.DO_NOTHING, db_column='id_acesso')
    senha = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'admin'


class Entrada(models.Model):
    id_e = models.BigAutoField(primary_key=True)
    id_acesso = models.ForeignKey(Acesso, models.DO_NOTHING, db_column='id_acesso')
    horario = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'entrada'


class Permanencia(models.Model):
    id_p = models.BigAutoField(primary_key=True)
    id_entrada = models.ForeignKey(Entrada, models.DO_NOTHING, db_column='id_entrada')
    id_saida = models.ForeignKey('Saida', models.DO_NOTHING, db_column='id_saida')

    class Meta:
        # managed = False
        db_table = 'permanencia'


class Pessoas(models.Model):
    id_pessoas = models.BigAutoField(primary_key=True)
    matricula = models.BigIntegerField(unique=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=50, blank=True, null=True)
    rfid = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'pessoas'

    def __str__(self):
        return self.nome

class Presente(models.Model):
    id_presente = models.BigAutoField(primary_key=True)
    id_acesso = models.ForeignKey(Acesso, models.DO_NOTHING, db_column='id_acesso')

    class Meta:
        # managed = False
        db_table = 'presente'


class Saida(models.Model):
    id_s = models.BigAutoField(primary_key=True)
    id_acesso = models.ForeignKey(Acesso, models.DO_NOTHING, db_column='id_acesso')
    horario = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'saida'
