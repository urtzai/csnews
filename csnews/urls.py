from django.conf.urls import patterns, url, include

from csnews.feeds import LatestNews
#feed_dict = {'rss': LatestNews}

urlpatterns = patterns('',
    (r'^$','csnews.views.index'),
    (r'^feed-(?P<url>.*)/$', LatestNews()),
    (r'^hemeroteka/', 'csnews.views.hemeroteka'),            
    url(r'^(?P<article_slug>[\-\d\w]+)/$','csnews.views.article_index', name='new_display'),
)

