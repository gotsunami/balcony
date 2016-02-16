# -*- coding: utf-8 -*-

from django.db import models
from django.utils.timezone import now

from balcony.models import Shortcut


class Slider(Shortcut):
    class Meta:
        verbose_name = u'Slider'
        verbose_name_plural = u'Sliders'
        ordering = ('-date_added',)
