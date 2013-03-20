from django.conf.urls.defaults import *

from csnews.feeds import LatestNews
#feed_dict = {'rss': LatestNews}

urlpatterns = patterns('',
    (r'^$','ahotsak.news.views.index'),
    (r'^feed-(?P<url>.*)/$', LatestNews()),
    (r'^hemeroteka/', 'ahotsak.news.views.hemeroteka'),            
    (r'^(?P<article_slug>[\-\d\w]+)/$','ahotsak.news.views.article_index'),
)

