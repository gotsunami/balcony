# -*- coding: utf-8 -*-

from django.utils.timezone import now
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.db import models

from ckeditor.fields import RichTextField

def smart_slugify(string, model, field='slug'):
    slugified = slugify(string)
    kwargs = {
        '{0}__{1}'.format(field, 'istartswith'): slugified,
    }
    conflicts = model.objects.filter(**kwargs).values_list(field, flat=True)
    if conflicts:
        identifier = 0
        base_slug = slugified
        while slugified in conflicts:
            identifier += 1
            slugified = u"{}-{}".format(base_slug, unicode(identifier))
    return slugified

class Tag(models.Model):
    value = models.CharField(max_length=32, verbose_name="Nom") 

    class Meta:
        verbose_name = u'Tag'
        verbose_name_plural = u'Tags'
        ordering = ('value',)

    def __unicode__(self):
        return unicode(self.value)

    def as_span(self, content_type):
        if content_type != None:
            count = content_type.objects.filter(tags=self).distinct().count()
        else:
            count = self.content_set.count()
        return {"badge": mark_safe(u"""<span class="badge">%d</span>""" % count), "label": mark_safe(self.value)}

class Content(models.Model):
    title = models.CharField(max_length=200, verbose_name=u"Titre")
    slug = models.CharField(max_length=200, verbose_name=u"Slug", unique=True)
    image = models.ImageField(verbose_name=u"Image", upload_to="content", null=True, blank=True)
    text = RichTextField(verbose_name=u"Contenu")
    summary = RichTextField(max_length=500, verbose_name=u"Résumé", null=True, blank=True)
    pub_date = models.DateTimeField(verbose_name=u"Publication", default=now)
    tags = models.ManyToManyField(Tag, verbose_name=u"tags")

    def smart_slugify(self):
        return smart_slugify(self.title, Content)
        if conflicts:
            identifier = 0
            base_slug = slugified
            while slugified in conflicts:
                identifier += 1
                slugified = u"{}-{}".format(base_slug, unicode(identifier))
        return slugified

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = self.smart_slugify()
        super(Content, self).save(force_insert, force_update, using, update_fields)

    def related(self):
        return type(self).objects.filter(tags__in=self.tags.all()).distinct().exclude(pk=self.pk)[:5]

    def related_tags(self):
        return [reduce(lambda x,y: dict(x, **y), ({"pk": tag.pk, }, tag.as_span(type(self)))) for tag in self.tags.all()]

    def all_tags(self):
        return [reduce(lambda x,y: dict(x, **y), ({"pk": tag.pk, }, tag.as_span(type(self)))) for tag in Tag.objects.filter(content__isnull=False).distinct()]

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return unicode(self.title)
