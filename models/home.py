# -*- coding: utf-8 -*-

from django.db import models
from django.utils.timezone import now

from balcony.models import Shortcut

class HomeBloc(Shortcut):
    class Meta:
        verbose_name = u'Argumentaire'
        verbose_name_plural = u'Argumentaires'
        ordering = ('date_added',)

class Badge(Shortcut):
    pass


class Home(models.Model):
    sliders = models.BooleanField(default=True, verbose_name=u"Show sliders")
    badges = models.BooleanField(default=True, verbose_name=u"Show badges")
    homeblocs = models.BooleanField(default=True, verbose_name=u"Show argumentaries")
