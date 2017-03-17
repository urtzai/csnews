from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from csnews.models import Article

ARTICLE_NUMBER_PER_PAGE = 20


def index(request):
    articles = Article.objects.filter(is_public=True)
    return render_to_response('news/articles.html', locals(), context_instance=RequestContext(request))


def article_index(request, article_slug):
    obj = get_object_or_404(Article, slug=article_slug)
    return render_to_response('news/article.html', locals(), context_instance=RequestContext(request))


def hemeroteka(request):
    return render_to_response('news/hemeroteka.html', locals(), context_instance=RequestContext(request))
