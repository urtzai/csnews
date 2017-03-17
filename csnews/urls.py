from django.conf.urls import url

from csnews.feeds import LatestNews

urlpatterns = [
    url(r'^$', 'csnews.views.index'),
    url(r'^feed-(?P<url>.*)/$', LatestNews()),
    url(r'^hemeroteka/', 'csnews.views.hemeroteka'),
    url(r'^(?P<article_slug>[\-\d\w]+)/$', 'csnews.views.article_index', name='new_display'),
]
