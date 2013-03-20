from django.db import models
from tagging.fields import TagField
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


class Article(models.Model):
    """Article model"""
    title  = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'),unique=True,db_index=True)
    published = models.DateTimeField(_('published'))
    summary = models.TextField(_('summary'), blank=True)
    body = models.TextField(_('body'))
    image = models.ForeignKey(Photo,null=True,blank=True,related_name=_('news image'))
        
    tags = TagField()

    is_public = models.BooleanField(default=True)
    allow_comments = models.BooleanField(_('allow comments'), default=True)

    added = models.DateField(_('added'),auto_now_add=True)
    modified = models.DateField(_('modified'),auto_now=True)
    sent_by_email =  models.BooleanField(default=False,editable=False)

    def get_title(self):
        return self.title

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering  = ('-published',)
        get_latest_by = 'published'


    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return "/albisteak/%s" % (self.slug)
    
def send_by_email(sender, instance, created,**kwargs):
    now = datetime.datetime.now()
    send = False
    if created:
        if instance.is_public and instance.published < now:
            send = True
    else:
        if instance.is_public and instance.published < now and not(instance.sent_by_email):
            send = True

    if send:
        subject = instance.title
        message = """
        %s

        %s
        """ % (instance.summary, instance.body)
        msgf = getattr(settings,'BULETIN_EMAIL',None)
        msgt = getattr(settings,'DEFAULT_POSTA_ZERRENDA',None)
        html_msg = render_to_string('news/article_by_mail.html',{'article':instance,'STATIC_URL':getattr(settings,'STATIC_URL'),'BASE_PATH':'www.ahotsak.com'})
        msg = EmailMultiAlternatives(subject, message, msgf, [msgt])
        msg.attach_alternative(html_msg, "text/html")
        msg.send()
        instance.sent_by_email=True
        instance.save()
post_save.connect(send_by_email, sender=Article)
