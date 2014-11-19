from django import forms
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.utils.html import escape
from django.template.defaultfilters import truncatewords


class PhotologueForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    """ """
    """
    def __init__(self, rel, attrs=None):
        super(PhotologueForeignKeyRawIdWidget, self).__init__(attrs)
        self.rel = rel  
    """
    def label_for_value(self, value):
        key = self.rel.get_related_field().name
        obj = self.rel.to._default_manager.get(**{key: value})
        try:
            img_url = obj.get_display_url()
        except:
            return '<br /><strong>%s</strong> ' % ('No display size defined')
        return '<br /><img src="%s" /> <br /><strong>%s</strong> ' % (img_url,escape(truncatewords(obj, 14)))        
