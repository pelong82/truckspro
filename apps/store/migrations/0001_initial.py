# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60, default='Baja California')),
                ('street', models.CharField(max_length=60)),
                ('number', models.IntegerField()),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('phone', models.CharField(max_length=60, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('address', models.ForeignKey(to='store.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Tire',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('measure', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=40)),
                ('serie', models.CharField(max_length=30)),
                ('design', models.CharField(max_length=30)),
            ],
        ),
    ]
