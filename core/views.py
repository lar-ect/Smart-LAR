# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from .models import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# from .forms import SignUpForm
import json
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

# Create your views here.

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)

@login_required(login_url="/login/")
def home(request):
    return render(request, 'index.html')


# @login_required
# def cadastro(request):
#     if request.method == "POST":
#         sign_up_form = SignUpForm(request.POST)

#         if sign_up_form.is_valid():
#             User = sign_up_form.save(commit=False)
#             User.save()

#             return redirect('core.views.home')
#     else:
#         sign_up_form = SignUpForm()

#     return render(request, 'forms.html', {'signup_form': SignUpForm})

@login_required
def get_data(request, usuario):
    # print(request.GET.get('id', 'not found'))
    print(usuario)
    # consulta no banco utilizando id

     # queryset = Pessoas.objects.all()
    # names = [obj.nome for obj in queryset]
    # acessos = Acesso.objects.all()
    names = ['Gabriel', 'Lucas', 'Tiago', 'Tibúrcio', 'Matheus', 'João']
    # query_entrada = Entrada.objects.all()
    #entradas = str([obj.horario for obj in query_entrada])
    entradas = [15, 18, 20, 10, 12, 14]
    #lista = serialize('json', entradas, cls=LazyEncoder)
    context = {
        'names': json.dumps(names),
        'entradas': json.dumps(entradas),
    }

    return JsonResponse(context, safe=False)

