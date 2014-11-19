from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from csnews.models import Article
from csnews.diggpaginator import DiggPaginator

import time
from datetime import datetime

ARTICLE_NUMBER_PER_PAGE = 20

def _get_page(list,page):
    """ """
    paginator = DiggPaginator(list, ARTICLE_NUMBER_PER_PAGE, body=5, padding=2)
    try:
        page = int(page)
    except ValueError:
        page = 1

    try:
        tor = paginator.page(page)
    except:
        tor = paginator.page(paginator.num_pages)
    return tor

def index(request):
    """ """
    h = {}
    
    h['articles'] = Article.objects.filter(is_public=True)
    h['page'] = _get_page(h['articles'],request.GET.get('orria', '1'))    
    return render_to_response('news/articles.html',h,context_instance=RequestContext(request))

def article_index(request,article_slug):
    """ """
    h = {}
    if request.LANGUAGE_CODE == 'eu':
        h['obj'] = get_object_or_404(Article, slug_eu = article_slug)
    else:
        h['obj'] = get_object_or_404(Article, slug_es = article_slug)
    return render_to_response('news/article.html',h,context_instance=RequestContext(request))

def hemeroteka(request):
    """ """
    h = {}
    return render_to_response('news/hemeroteka.html',h,context_instance=RequestContext(request))
