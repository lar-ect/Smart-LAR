# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Pessoas)
admin.site.register(Permanencia)
admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(Acesso)
