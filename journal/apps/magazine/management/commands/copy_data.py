# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.contrib.contenttypes.models import ContentType

from journal.apps.magazine.models import Article, Journal, Number, Rubric, Text, Type

class Command(BaseCommand):

    help = u"Переписываем данные из старой базы в новую"
    args = ""

    @transaction.commit_on_success
    def handle(self, *args, **options):

        cursor = connection.cursor()

#        cursor.execute('SELECT * FROM "modulJournalType" ORDER BY id')
#        rowset = cursor.fetchall()
##        c_t = ContentType.objects.get_for_model(Route)
#        for row in rowset:
#            print row
#
#            type, status = Type.objects.get_or_create(
#                title=row[1],
#                slug=row[2]
#            )
#
#            print status, type


#        cursor.execute('SELECT * FROM "modulJournal" ORDER BY id')
#        rowset = cursor.fetchall()
#        for row in rowset:
#            type = Type.objects.get(pk=row[1])
#            journal, status = Journal.objects.get_or_create(
#                type=type,
#                title=row[2],
#                slug=row[3],
#                note=row[4],
#                cnt_view=row[5]
#            )
#            print status

#        cursor.execute('SELECT * FROM "modulJournalRubric" ORDER BY id')
#        rowset = cursor.fetchall()
#        for row in rowset:
#            journal = Journal.objects.get(pk=row[3])
#            journal, status = Rubric.objects.get_or_create(
#                pk=row[0],
#                journal=journal,
#                title=row[1]
#            )
#            print status

#        cursor.execute('SELECT * FROM "modulJournalNumber" ORDER BY id')
#        rowset = cursor.fetchall()
#        for row in rowset:
#            journal = Journal.objects.get(pk=row[1])
#            number, status = Number.objects.get_or_create(
#                pk=row[0],
#                journal=journal,
#                year=row[2],
#                number=row[3]
#            )
#            print status

#        cursor.execute('SELECT * FROM "modulJournalArticle" ORDER BY id')
#        rowset = cursor.fetchall()
#        for row in rowset:
#            journal = Journal.objects.get(pk=row[8])
#            number = Number.objects.get(pk=row[1])
#            rubric = Rubric.objects.get(pk=row[2])
#            article, status = Article.objects.get_or_create(
#                pk=row[0],
#                journal=journal,
#                number=number,
#                rubric=rubric,
#                title=row[3],
#                author=row[4],
#                source=row[5],
#                page=row[6],
#                text=row[9],
#                cnt_view=row[10]
#            )
#            print status

#        cursor.execute('SELECT * FROM "modulJournalText" ORDER BY id')
#        rowset = cursor.fetchall()
#        for row in rowset:
#            article = Article.objects.get(pk=row[1])
#            text, status = Text.objects.get_or_create(
#                pk=row[0],
#                article=article,
#                text=row[2],
#            )
#            print status