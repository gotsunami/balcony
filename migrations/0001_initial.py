# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('slug', models.CharField(unique=True, max_length=200, verbose_name='Slug')),
                ('image', models.ImageField(upload_to=b'content', null=True, verbose_name='Image', blank=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Contenu')),
                ('summary', ckeditor.fields.RichTextField(max_length=500, null=True, verbose_name='R\xe9sum\xe9', blank=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Titre', blank=True)),
                ('order', models.IntegerField(verbose_name='Position, entre 1 et 3')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Pied de page',
                'verbose_name_plural': 'Pieds de page',
            },
        ),
        migrations.CreateModel(
            name='Shortcut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Titre', blank=True)),
                ('image', models.ImageField(upload_to=b'shortcut', null=True, verbose_name='Image', blank=True)),
                ('text', ckeditor.fields.RichTextField(null=True, verbose_name='Texte', blank=True)),
                ('url', models.CharField(help_text='Lien vers lequel doit pointer le bouton (hyperlien ou balise)', max_length=200, null=True, verbose_name='Url', blank=True)),
                ('button_text', models.CharField(max_length=50, null=True, verbose_name='Texte du bouton', blank=True)),
                ('active', models.BooleanField(default=True, help_text="D\xe9fini si l'\xe9l\xe9ment doit s'afficher ou non", verbose_name='Actif')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'ajout")),
            ],
            options={
                'ordering': ('-date_added',),
                'verbose_name': 'Raccourci',
                'verbose_name_plural': 'Raccourcis',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=32, verbose_name=b'Nom')),
            ],
            options={
                'ordering': ('value',),
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('shortcut_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='balcony.Shortcut')),
            ],
            bases=('balcony.shortcut',),
        ),
        migrations.CreateModel(
            name='FooterShortcut',
            fields=[
                ('shortcut_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='balcony.Shortcut')),
                ('footer', models.ForeignKey(related_name='shortcut', to='balcony.Footer')),
            ],
            bases=('balcony.shortcut',),
        ),
        migrations.CreateModel(
            name='HomeBloc',
            fields=[
                ('shortcut_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='balcony.Shortcut')),
            ],
            options={
                'ordering': ('date_added',),
                'verbose_name': 'Argumentaire',
                'verbose_name_plural': 'Argumentaires',
            },
            bases=('balcony.shortcut',),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('shortcut_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='balcony.Shortcut')),
            ],
            options={
                'ordering': ('-date_added',),
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
            bases=('balcony.shortcut',),
        ),
        migrations.AddField(
            model_name='shortcut',
            name='page',
            field=models.ForeignKey(related_name='shortcut', verbose_name='Page', blank=True, to='balcony.Content', null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(to='balcony.Tag', verbose_name='tags'),
        ),
    ]
