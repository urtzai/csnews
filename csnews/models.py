from django.db import models
from django.utils.translation import ugettext_lazy as _
from photologue.models import Photo
from django.db.models.signals import post_save
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from transmeta import TransMeta


class Article(models.Model):
    __metaclass__ = TransMeta
    
    title  = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'),unique=True,db_index=True)
    published = models.DateTimeField(_('published'))
    summary = models.TextField(_('summary'), blank=True)
    body = models.TextField(_('body'))
    image = models.ForeignKey(Photo,null=True,blank=True,related_name=_('news image'))
        
    is_public = models.BooleanField(default=True)

    added = models.DateField(_('added'),auto_now_add=True)
    modified = models.DateField(_('modified'),auto_now=True)

    def get_title(self):
        return self.title

    class Meta:
        translate = ('title', 'slug', 'summary','body')
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering  = ('-published',)
        get_latest_by = 'published'


    def __unicode__(self):
        return u'%s' % self.title
    
