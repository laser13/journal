# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

import datetime
from hashlib import md5
from django.db import models
from tagging.fields import TagField

class Type(models.Model):

    title = models.CharField(max_length=255, verbose_name=u'Название')
    slug = models.SlugField(max_length=64)

    def __unicode__(self):
        return self.title

class Journal(models.Model):

    type = models.ForeignKey(Type, related_name='%(class)s')
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    slug = models.SlugField(max_length=64)
    note = models.TextField(null=True)
    cnt_view = models.PositiveIntegerField(default=0, verbose_name=u'Количество просмотров', editable=False)

class Number(models.Model):

    journal = models.ForeignKey(Journal)
    year = models.PositiveSmallIntegerField(max_length=4, verbose_name=u'Год выхода журнала')
    number = models.PositiveSmallIntegerField(max_length=2, verbose_name=u'Номер журнала')

    @models.permalink
    def get_absolute_url(self):
        return ('number.show', (), {'number_id':self.pk})

    def get_random_article(self):
        return self.article_number.all()[0]

    def get_name(self):
        return u'{0} ({1} за {2} год)'.format(self.journal.title, self.number, self.year)

    random_article = property(get_random_article)
    name = property(get_name)

class NumberCover(models.Model):

    CHOICES_TYPE = (
        (1, u'Обложка лицевая',),
        (2, u'Обложка оборотная',),
    )

    def upload_cover_image(obj, filename):
        ext = filename.split('.').pop()
        now = '{0}'.format(datetime.datetime.now())
        name = md5(now).hexdigest()
        return 'img/number/{0}/{1}.{2}'.format(obj.number.year, name, ext)

    number = models.ForeignKey(Number)
    image = models.ImageField(upload_to=upload_cover_image, null=True, default=None)
    type = models.PositiveSmallIntegerField(choices=CHOICES_TYPE)
    note = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    cnt_view = models.PositiveIntegerField(default=0, verbose_name=u'Количество просмотров', editable=False)

    class Meta:
        ordering = ['type']

    @models.permalink
    def get_absolute_url(self):
        return ('cover.show', (), {'cover_id':self.pk})

class Rubric(models.Model):

    journal = models.ForeignKey(Journal, related_name='%(class)s')
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')

    @models.permalink
    def get_absolute_url(self):
        return ('rubric.show', (), {'rubric_id':self.pk})

class Article(models.Model):

    journal = models.ForeignKey(Journal)
    number = models.ForeignKey(Number)
    rubric = models.ForeignKey(Rubric)
    page = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    author = models.CharField(max_length=255, verbose_name=u'Автор статьи', null=True, blank=True)
    source = models.CharField(max_length=255, verbose_name=u'Источник', null=True, blank=True)
    text = models.TextField()
    tags = TagField()
    cnt_view = models.PositiveIntegerField(default=0, verbose_name=u'Количество просмотров', editable=False)

    class Meta:
        ordering = ['page']

    @models.permalink
    def get_absolute_url(self):
        return ('article.show', (), {'article_id':self.pk})

    def get_first_text(self):
        return self.text_set.all()[0]

    first_text = property(get_first_text)

class Text(models.Model):

    article = models.ForeignKey(Article, related_name='%(class)s_set')
    text = models.TextField()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.text


class ArticleImage(models.Model):

    def upload_article_image(object, filename):
        ext = filename.split('.').pop()
        now = '{0}'.format(datetime.datetime.now())
        name = md5(now).hexdigest()
        return 'img/article/{0:d}/{1}.{2}'.format(object.article.pk, name, ext)

    article = models.ForeignKey(Article)
    image = models.ImageField(upload_to=upload_article_image)
    note = models.TextField(verbose_name=u'Описание')
    cnt_view = models.PositiveIntegerField(default=0, verbose_name=u'Количество просмотров', editable=False)

    @models.permalink
    def get_absolute_url(self):
        return ('image.show', (), {'image_id':self.pk})