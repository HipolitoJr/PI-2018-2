# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-27 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buscas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resultados',
            new_name='Resultado',
        ),
    ]