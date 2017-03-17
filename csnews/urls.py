from django.conf.urls import url
from csnews import views
from csnews.feeds import LatestNews

urlpatterns = [
    url(r'^$', views.index, name="csnews_index"),
    url(r'^feed$', LatestNews(), name="csnews_feed"),
    url(r'^archive/', views.archive, name="csnews_archive"),
    url(r'^(?P<article_slug>[\-\d\w]+)/$', views.article_index, name='csnews_display'),
]
