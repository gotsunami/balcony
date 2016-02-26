# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.text import mark_safe

from balcony.models import Footer, FooterShortcut

class FooterShortcutInline(admin.TabularInline):
    fields = ['page', 'title']
    model = FooterShortcut

class FooterAdmin(admin.ModelAdmin):
    list_display = ['title']

    inlines = [FooterShortcutInline, ]

admin.site.register(Footer, FooterAdmin)
