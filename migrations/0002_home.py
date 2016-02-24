# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balcony', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sliders', models.BooleanField(default=True, verbose_name='Show sliders')),
                ('badges', models.BooleanField(default=True, verbose_name='Show badges')),
                ('homeblocs', models.BooleanField(default=True, verbose_name='Show argumentaries')),
            ],
        ),
    ]
