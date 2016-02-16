# -*- coding: utf-8 -*-

from django.db import models

from balcony.models import Shortcut

class Footer(models.Model):
    title = models.CharField(max_length=200, verbose_name=u"Titre", null=True, blank=True)
    order = models.IntegerField(verbose_name=u"Position, entre 1 et 3")


    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Pied de page'
        verbose_name_plural = u'Pieds de page'
        ordering = ["order",]
    
class FooterShortcut(Shortcut):
    footer = models.ForeignKey(Footer, related_name="shortcut")
    
