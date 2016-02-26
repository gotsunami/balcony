# -*- coding: utf-8 -*-

from django.db import models

from balcony.models import Shortcut

class Footer(models.Model):
    title = models.CharField(max_length=200, verbose_name=u"Title", null=True, blank=True)
    order = models.IntegerField(verbose_name=u"Position")


    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Footer'
        verbose_name_plural = u'Footers'
        ordering = ["order",]
    
class FooterShortcut(Shortcut):
    footer = models.ForeignKey(Footer, related_name="shortcut")
    
