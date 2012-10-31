# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'


from django.core.management.base import BaseCommand
from django.db import connection, transaction

from journal.settings import STATIC_PATH
import os

from journal.apps.magazine.models import Article
from django.core.files.base import ContentFile

class Command(BaseCommand):

    help = u"Переписываем данные из старой базы в новую"
    args = ""

    @transaction.commit_on_success
    def handle(self, *args, **options):

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "modulTag"')
        rowset = cursor.fetchall()

        for row in rowset:
           sql = 'INSERT INTO "tagging_tag" VALUES '