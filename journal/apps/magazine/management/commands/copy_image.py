# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'


from django.core.management.base import BaseCommand
from django.db import connection, transaction

from journal.settings import STATIC_PATH
import os

from journal.apps.magazine.models import ArticleImage, Article, Number, NumberCover
from django.core.files.base import ContentFile

class Command(BaseCommand):

    help = u"Переписываем данные из старой базы в новую"
    args = ""

    @transaction.commit_on_success
    def handle(self, *args, **options):

        path = os.path.join(STATIC_PATH, 'tmp')

        cursor = connection.cursor()
#        cursor.execute('SELECT * FROM "modulImage" WHERE "modulID"=4 ORDER BY id')
#        rowset = cursor.fetchall()
#        for row in rowset:
#            article_id = row[2]
#            name = row[3]
#            alt = row[6]
#            cnt_view = row[12]
#
#            article = Article.objects.get(pk=article_id)
#
#            file = os.path.join(path, name + '.jpg')
#
#            art_image, status = ArticleImage.objects.get_or_create(
#                pk=row[0],
#                article=article,
#                note=alt,
#                cnt_view=cnt_view
#            )
#
#            print status
#
#            if status or art_image:
#                art_image.image.save('.jpg', ContentFile(open(file, 'rb').read()))
#                art_image.save()
#
#                print 'ok'

        cursor.execute('SELECT * FROM "modulImage" WHERE "modulID"=2 ORDER BY id')
        rowset = cursor.fetchall()
        for row in rowset:
            number_id = row[2]
            name = row[3]
            alt = row[6]
            cnt_view = row[12]

            type = row[11]



            if type == "coverFirst":
                type = 1
            if type == "coverLast":
                type = 2

            print type, alt

            number = Number.objects.get(pk=number_id)

            file = os.path.join(path, name + '.jpg')

            num_cover, status = NumberCover.objects.get_or_create(
                pk=row[0],
                number=number,
                note=alt,
                type=type,
                cnt_view=cnt_view
            )

            print status, num_cover, file

            if status or num_cover:
                num_cover.image.save('.jpg', ContentFile(open(file, 'rb').read()))
                num_cover.save()

                print 'ok'