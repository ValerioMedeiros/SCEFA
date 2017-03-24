# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-24 16:56
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('Email', models.EmailField(max_length=200, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('matricula', models.CharField(max_length=10, unique=True, verbose_name='Matricula')),
                ('senha', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrarPonto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField(default=django.utils.timezone.now)),
                ('saida', models.DateTimeField(default=django.utils.timezone.now)),
                ('local', models.CharField(max_length=200, verbose_name='local')),
            ],
            options={
                'permissions': (('view_relatorio', 'Can see relatorio'), ('view_relatorioPonto', 'Can see relatorio a mais')),
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appPonto.Pessoa')),
            ],
            options={
                'permissions': (('view_administrador', 'Can see Administrador'),),
            },
            bases=('appPonto.pessoa',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appPonto.Pessoa')),
            ],
            options={
                'permissions': (('view_funcionario', 'Can see aluno'),),
            },
            bases=('appPonto.pessoa',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='registrarponto',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPonto.Funcionario', verbose_name='Funcionario'),
        ),
    ]
