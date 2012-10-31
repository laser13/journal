# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

from django.contrib import admin
from django.contrib.contenttypes import generic

from journal.apps.magazine.models import Journal, Article, Number, Rubric, Text, Type, ArticleImage

class JournalAdmin(admin.ModelAdmin):

    list_display = ('title', 'type', 'cnt_view',)
    list_filter = ('type__title',)
#    search_fields = ('note__name',)
    ordering = ('title',)



admin.site.register(Journal, JournalAdmin)