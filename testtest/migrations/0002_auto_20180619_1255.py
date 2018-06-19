# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='objectflat',
            name='lift',
            field=models.CharField(choices=[('yes', 'есть'), ('no', 'нет'), ('hz', '')], default='hz', max_length=20),
        ),
        migrations.AlterField(
            model_name='objectflat',
            name='parking',
            field=models.CharField(choices=[('yes', 'во дворе'), ('no', 'нет'), ('hz', '')], default='hz', max_length=20),
        ),
        migrations.AlterField(
            model_name='objectflat',
            name='wall_material',
            field=models.CharField(choices=[('kirp', 'кирпич'), ('pan', 'панель'), ('nd', '')], default='нет данных', max_length=20),
        ),
    ]