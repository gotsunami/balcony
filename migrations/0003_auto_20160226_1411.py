# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('balcony', '0002_home'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Homepage', 'verbose_name_plural': 'Homepage'},
        ),
        migrations.AddField(
            model_name='home',
            name='header_color',
            field=colorfield.fields.ColorField(default=b'#3264AD', max_length=10),
        ),
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(upload_to=b'shortcut', null=True, verbose_name='Image', blank=True),
        ),
    ]
