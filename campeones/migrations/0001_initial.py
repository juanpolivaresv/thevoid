# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeon',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(help_text=b'Escribe el nombre del campeon', max_length=64)),
                ('descripcion', models.CharField(help_text=b'Escribe la descripcion del campeon', max_length=256)),
                ('slug', models.SlugField(max_length=256, editable=False)),
                ('avatar', models.ImageField(upload_to=b'campeones/static/img/avatar')),
                ('splash', models.ImageField(upload_to=b'campeones/static/img/splash')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(help_text=b'Escribe el nombre del rol', max_length=64)),
                ('descripcion', models.CharField(help_text=b'Escribe la descripcion del rol', max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='campeon',
            name='rol',
            field=models.ForeignKey(related_name='rol', to='campeones.Rol'),
        ),
        migrations.AddField(
            model_name='campeon',
            name='rol_secundario',
            field=models.ForeignKey(related_name='rol_secundario', blank=True, to='campeones.Rol', null=True),
        ),
    ]
