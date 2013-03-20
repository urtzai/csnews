from django.conf.urls.defaults import *

from csnews.feeds import LatestNews
#feed_dict = {'rss': LatestNews}

urlpatterns = patterns('',
    (r'^$','ahotsak.news.views.index'),
    (r'^feed-(?P<url>.*)/$', LatestNews()),
    (r'^hemeroteka/', 'ahotsak.news.views.hemeroteka'),  
    url(r'^eguneko-bideoa/$', 'ahotsak.news.views.eguneko_pasartea_index',name='eguneko_pasartea_index'),
    url(r'^eguneko-bideoa/(?P<data>[\-\d\w]+)/$', 'ahotsak.news.views.eguneko_pasartea',name='eguneko_pasartea'),          
    (r'^(?P<article_slug>[\-\d\w]+)/$','ahotsak.news.views.article_index'),
)

