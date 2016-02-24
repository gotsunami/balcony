# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.messages import SUCCESS

from balcony.models import Home, Badge, HomeBloc

class HomeBlocAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'date_added']
    list_filter = ['active', 'date_added']
    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        updated_rows = queryset.update(active=True)
        if updated_rows == 1:
            message = u"1 bloc a été activé"
        else:
            message = u"{} blocs ont été activés".format(updated_rows)
        self.message_user(request, message=message, level=SUCCESS)
    activate.short_description = u"Activer les blocs séléctionnés"

    def deactivate(self, request, queryset):
        updated_rows = queryset.update(active=False)
        if updated_rows == 1:
            message = u"Un bloc slide a été desactivé"
        else:
            message = u"{} blocs ont été desactivés".format(updated_rows)
        self.message_user(request, message=message, level=SUCCESS)
    deactivate.short_description = u"Desactiver les blocs séléctionnés"

admin.site.register(Badge, HomeBlocAdmin)
admin.site.register(HomeBloc, HomeBlocAdmin)
admin.site.register(Home)
