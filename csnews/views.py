from django.shortcuts import render
from django.shortcuts import get_object_or_404

from csnews.models import Article

ARTICLE_NUMBER_PER_PAGE = 20


def index(request):
    articles = Article.objects.filter(is_public=True)
    return render(request, 'news/articles.html', locals())


def article_index(request, article_slug):
    obj = get_object_or_404(Article, slug=article_slug)
    return render(request, 'news/article.html', locals())


def archive(request):
    return render(request, 'news/archive.html', locals())
