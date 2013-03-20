from photologue.models import Photo
from urllib2 import urlopen
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile

from random import  randint

def _getUrlImage(url):
    """ """
    try:
        socket = urlopen(url)
    except:
        socket = None
    return socket 


def loadUrlImage(url='', title='', tags='', format='jpg'):
    """ """
    if not url:
        url = 'http://ahotsak.com/files/Proiektuak/beasain.jpg'
        title = 'Beasain'
        tags = 'proiektua beasain'

    slug = slugify(title)[:50]

    image = _getUrlImage(url)

    if not image:
        return 0

    if Photo.objects.filter(title_slug=slug):
        for i in range(1,1000):
            new_slug = '%s-%d' % (slug,i)
            new_title = '%s (%d)' % (title,i)
            if not Photo.objects.filter(title_slug=new_slug):
                slug = new_slug
                title = new_title
                break
        
    photo = Photo()
    photo.title = title
    photo.tags = tags
    photo.title_slug = slug
    photo.image.save('%s.%s' % (slug,format), ContentFile(image.read()))
    try:
        photo.save()
    except:
        print 'Errorea irudi honekin', photo.title
        """
        photo.title_slug = photo.title_slug + '_2'         
        photo.save()
        """
    return photo
