# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.


class Cadastro(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    matricula = models.CharField(max_length=255, null=False, blank=False)
    rfid = models.CharField(max_length=255)

    class Meta:
	    db_table = "lar_cadastro"

