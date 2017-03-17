from django.db import models
from django.utils.translation import ugettext_lazy as _
from photologue.models import Photo


class Article(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique=True, db_index=True)
    published = models.DateTimeField(_('published'))
    summary = models.TextField(_('summary'), blank=True)
    body = models.TextField(_('body'))
    image = models.ForeignKey(Photo, null=True, blank=True, related_name=_('news_image'))

    is_public = models.BooleanField(default=True)

    added = models.DateField(_('added'), auto_now_add=True)
    modified = models.DateField(_('modified'), auto_now=True)

    def get_title(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ('-published',)
        get_latest_by = 'published'
