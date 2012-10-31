# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

from django.conf.urls import *
from views import *

urlpatterns = patterns('journal.apps.magazine.views',

    url(r'^$', 'index', name='magazine.index'),

    url(r'number/(?P<number_id>[\d]+)/$', 'number', name='number.show'),
    url(r'rubric/(?P<rubric_id>[\d]+)/$', 'rubric', name='rubric.show'),
    url(r'article/(?P<article_id>[\d]+)/$', 'article', name='article.show'),
    url(r'article/(?P<article_id>[\d]+)/(?P<page>[\d]+)/$', 'article', name='text.show'),
    url(r'image/(?P<image_id>[\d]+)/$', 'image', name='image.show'),
    url(r'cover/(?P<cover_id>[\d]+)/$', 'cover', name='cover.show'),

#    url(r'data/(?P<interval>[\w]+)/(?P<user_id>[\d]+)/$', 'data', name='photoline.data'),
#    url(r'data/(?P<interval>[\w]+)/$', 'data', name='photoline.data'),
#    url(r'data/$', 'data', name='photoline.data'),
#
#    url(r'set_position/(?P<picture_id>[\d]+)', 'set_position', name='photo.set_position'),
#    url(r'show/(?P<picture_id>[\d]+)', 'show', name='photo.show'),
#    url(r'^line/(?P<picture_id>[\d]+)/', 'line', name='photo.userline'),
#
#    url(r'add/$', 'add', name='photoline.add'),
#    url(r'preload/$', 'preload', name='photoline.preload'),
#
#    url(r'^line/', 'line', name='photoline.userline'),
#    url(r'^area/', 'area', name='photoline.userarea'),
#    url(r'^year/', 'by_year', name='photoline.user_by_year'),
#    url(r'^month/', 'by_month', name='photoline.user_by_month'),
#    url(r'^week/', 'by_week', name='photoline.user_by_week'),
#    url(r'^day/', 'by_day', name='photoline.user_by_day'),
#
#    url(r'(?P<picture_id>[\d]+)/update_comments/$', 'update_comments', name='photo.update_comments'),
#    url(r'(?P<picture_id>[\d]+)/edit/$', 'edit', name='photo.edit'),
#    url(r'(?P<picture_id>[\d]+)/delete/$', 'delete', name='photo.delete'),
#    url(r'(?P<picture_id>[\d]+)/$', 'read', name='photo.read'),
#    #    url(r'login/$', 'enter', name='main.login'),
#    #    url(r'logout/$', 'output', name='main.logout'),

)