# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 17:39
from __future__ import unicode_literals

import app.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161102_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='R_Objekt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(max_length=500)),
                ('caption', models.TextField(max_length=500)),
                ('date', app.forms.FormattedDateField()),
            ],
        ),
    ]
