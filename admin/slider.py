# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.messages import SUCCESS

from balcony.models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ['page', 'title', 'active', 'date_added']
    list_filter = ['active', 'date_added']
    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        updated_rows = queryset.update(active=True)
        if updated_rows == 1:
            message = u"1 slide été activée"
        else:
            message = u"{} slides ont été activées".format(updated_rows)
        self.message_user(request, message=message, level=SUCCESS)
    activate.short_description = u"Activer les slides séléctionées"

    def deactivate(self, request, queryset):
        updated_rows = queryset.update(active=False)
        if updated_rows == 1:
            message = u"Une slide été desactivée"
        else:
            message = u"{} slides ont été desactivées".format(updated_rows)
        self.message_user(request, message=message, level=SUCCESS)
    deactivate.short_description = u"Desactiver les slides séléctionnées"

admin.site.register(Slider, SliderAdmin)
