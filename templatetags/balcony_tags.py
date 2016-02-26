# -*- coding: utf-8 -*-
from django import template
from django.core import urlresolvers

from balcony.models import Home

register = template.Library()

@register.assignment_tag
def balcony_settings():
    home = Home.objects.all()
    if home.count():
        home = home[0]
    else:
        home = Home()
        home.save()

    return home
