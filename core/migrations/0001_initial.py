# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id_a', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'acesso',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_admin', models.BigAutoField(primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=255)),
                ('id_acesso', models.ForeignKey(db_column='id_acesso', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Acesso')),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id_e', models.BigAutoField(primary_key=True, serialize=False)),
                ('horario', models.DateTimeField()),
                ('id_acesso', models.ForeignKey(db_column='id_acesso', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Acesso')),
            ],
            options={
                'db_table': 'entrada',
            },
        ),
        migrations.CreateModel(
            name='Permanencia',
            fields=[
                ('id_p', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_entrada', models.ForeignKey(db_column='id_entrada', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Entrada')),
            ],
            options={
                'db_table': 'permanencia',
            },
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id_pessoas', models.BigAutoField(primary_key=True, serialize=False)),
                ('matricula', models.BigIntegerField(unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('rfid', models.CharField(blank=True, max_length=15, null=True, unique=True)),
            ],
            options={
                'db_table': 'pessoas',
            },
        ),
        migrations.CreateModel(
            name='Presente',
            fields=[
                ('id_presente', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_acesso', models.ForeignKey(db_column='id_acesso', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Acesso')),
            ],
            options={
                'db_table': 'presente',
            },
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id_s', models.BigAutoField(primary_key=True, serialize=False)),
                ('horario', models.DateTimeField()),
                ('id_acesso', models.ForeignKey(db_column='id_acesso', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Acesso')),
            ],
            options={
                'db_table': 'saida',
            },
        ),
        migrations.AddField(
            model_name='permanencia',
            name='id_saida',
            field=models.ForeignKey(db_column='id_saida', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Saida'),
        ),
        migrations.AddField(
            model_name='acesso',
            name='id_pes',
            field=models.ForeignKey(db_column='id_pes', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Pessoas'),
        ),
    ]
