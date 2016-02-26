# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('balcony', '0003_auto_20160226_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='badges_color',
            field=colorfield.fields.ColorField(default=b'#3264AD', max_length=10, verbose_name='Badges background color'),
        ),
        migrations.AddField(
            model_name='home',
            name='homeblocs_color',
            field=colorfield.fields.ColorField(default=b'#EEEEEE', max_length=10, verbose_name='Main background color'),
        ),
        migrations.AddField(
            model_name='home',
            name='sliders_color',
            field=colorfield.fields.ColorField(default=b'#3264AD', max_length=10, verbose_name='Slideshow background color'),
        ),
        migrations.AlterField(
            model_name='home',
            name='header_color',
            field=colorfield.fields.ColorField(default=b'#3264AD', max_length=10, verbose_name='Header background color'),
        ),
    ]
