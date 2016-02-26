# -*- coding: utf-8 -*-

from django.db import models

from ckeditor.fields import RichTextField

from balcony.models import Shortcut

class Footer(models.Model):
    title = models.CharField(max_length=200, verbose_name=u"Title", null=True, blank=True)
    text = RichTextField(verbose_name=u"Texte", null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Footer'
        verbose_name_plural = u'Footers'
    
class FooterShortcut(Shortcut):
    footer = models.ForeignKey(Footer, related_name="shortcuts")
    
