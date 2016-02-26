# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('balcony', '0004_auto_20160226_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Footer', 'verbose_name_plural': 'Footers'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Global settings', 'verbose_name_plural': 'Global settings'},
        ),
        migrations.AlterModelOptions(
            name='homebloc',
            options={'ordering': ('date_added',), 'verbose_name': 'Argumentary', 'verbose_name_plural': 'Argumentaries'},
        ),
        migrations.RemoveField(
            model_name='footer',
            name='order',
        ),
        migrations.AddField(
            model_name='footer',
            name='text',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Texte', blank=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='badges_color',
            field=colorfield.fields.ColorField(default=b'#3264AD', max_length=10, verbose_name='Background color'),
        ),
        migrations.AlterField(
            model_name='home',
            name='header_color',
            field=colorfield.fields.ColorField(default=b'#3264AD', max_length=10, verbose_name='Background color'),
        ),
        migrations.AlterField(
            model_name='home',
            name='homeblocs_color',
            field=colorfield.fields.ColorField(default=b'#EEEEEE', max_length=10, verbose_name='Background color'),
        ),
        migrations.AlterField(
            model_name='home',
            name='sliders_color',
            field=colorfield.fields.ColorField(default=b'#3264AD', max_length=10, verbose_name='Background color'),
        ),
        migrations.AlterField(
            model_name='shortcut',
            name='page',
            field=models.ForeignKey(related_name='shortcut', verbose_name='Page', blank=True, to='pages.Page', null=True),
        ),
    ]
