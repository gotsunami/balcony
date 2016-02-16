# -*- coding: utf-8 -*-

from django.db import models
from django.utils.timezone import now

from ckeditor.fields import RichTextField

from balcony.models import Content


class Shortcut(models.Model):
    page = models.ForeignKey(Content, related_name="shortcut", verbose_name=u"Page", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name=u"Titre", null=True, blank=True)
    image = models.ImageField(verbose_name=u"Image", upload_to="shortcut", null=True, blank=True)
    text = RichTextField(verbose_name=u"Texte", null=True, blank=True)
    url = models.CharField(max_length=200, verbose_name=u"Url", help_text=u"Lien vers lequel doit pointer le bouton (hyperlien ou balise)", null=True,
                          blank=True)
    button_text = models.CharField(max_length=50, verbose_name=u"Texte du bouton", null=True, blank=True)
    active = models.BooleanField(verbose_name=u"Actif", help_text=u"Défini si l'élément doit s'afficher ou non",
                                 default=True)
    date_added = models.DateTimeField(verbose_name=u"Date d'ajout", default=now)

    class Meta:
        verbose_name = u'Raccourci'
        verbose_name_plural = u'Raccourcis'
        ordering = ('-date_added',)
    
    def __unicode__(self):
        return unicode(self.title)
