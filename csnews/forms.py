from django import forms
from django.conf import settings
from tinymce.widgets import TinyMCE
from csnews.models import Article

TINYMCE_DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', {})


class ArticleAdminForm(forms.ModelForm):
    desk = forms.CharField(widget=TinyMCE(
                           attrs={'cols': 80, 'rows': 50, }, mce_attrs=TINYMCE_DEFAULT_CONFIG))

    class Meta:
        model = Article
        fields = '__all__'
