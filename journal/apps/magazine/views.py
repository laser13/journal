# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.views.decorators.cache import cache_page
from models import Number, Article, Journal, ArticleImage, Rubric, NumberCover
from tagging.models import Tag, TaggedItem

@cache_page(60 * 24)
def index(request):

    numbers = Number.objects.all().select_related()

    return render(request, 'magazine/index.html', locals())

def number(request, number_id):

    number = get_object_or_404(Number, pk=number_id)

    return render(request, 'magazine/number.html', locals())

def rubric(request, rubric_id):

    rubric = get_object_or_404(Rubric, pk=rubric_id)

    return render(request, 'magazine/rubric.html', locals())

def article(request, article_id, page=0):

    page = int(page)
    article = get_object_or_404(Article, pk=article_id)
    Article.objects.filter(pk=article_id).update(cnt_view=F('cnt_view') + 1)

    text = article.text_set.all()[page]
    count = article.text_set.count() - 1

    next = prev = None
    if page < count:
        next = page + 1
        if page > 0:
            prev = page - 1
    else:
        prev = page - 1

    return render(request, 'magazine/article.html', locals())

def image(request, image_id):

    image = get_object_or_404(ArticleImage, pk=image_id)
    ArticleImage.objects.filter(pk=image_id).update(cnt_view=F('cnt_view') + 1)

    return render(request, 'magazine/image.html', locals())

def cover(request, cover_id):

    cover = get_object_or_404(NumberCover, pk=cover_id)

    return render(request, 'magazine/cover.html', locals())

def tag(request, tag_id):

    tag = get_object_or_404(Tag, pk=tag_id)
    articles = TaggedItem.objects.get_by_model(Article, tag)

    return render(request, 'magazine/tag.html', locals())