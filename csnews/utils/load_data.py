from csnews.utils.load_images import loadUrlImage
from csnews.models import Article
from lxml import etree
from django.template.defaultfilters import slugify
from django.conf import settings

from datetime import datetime

#BASE_PATH = 'http://www.ahotsak.com/news'
#END_PATH = 'export.xml'

   
def get_news():
    path = '%s/%s' % (settings.BASE_PATH, settings.END_PATH)
    coords = etree.parse(path).getroot()

    all = []
    for coord in coords:
        this = {}
        for child in coord.getchildren():
            this[child.tag] = child.text
        all.append(this)
    return all
    

def get_datetime_from_string(s):
    """ """
    f = '%Y/%m/%d %H:%M:%S'
    return datetime.strptime(s,f)

def load_news():
    """ """
    for new in get_news():
        try:
            image_url = new['image_url']
            image_format = image_url[-3:]
            photo = loadUrlImage(image_url, 'Albistea: %s' % new['title'], 'albistea',image_format)
        except:
            photo = None
        article = Article()
        article.title=new['title']
        article.summary = new['summary']
        article.body = new['body']
        article.slug = slugify(article.title)[:50]
        sdate = new['date']
        sdate = ' '.join(sdate.split(' ')[:-1])        
        article.published = get_datetime_from_string(sdate)
        if photo:
            article.image = photo
        article.tags = new['author'].lower()
        article.save()
        print article.title
    return 1 
