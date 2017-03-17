from django.contrib import admin
from csnews.models import Article
from django.conf import settings

from tinymce.widgets import TinyMCE


def show_entry_thumbnail(item):
    if item.image:
        return item.image.admin_thumbnail()
    else:
        return None
    # return item.admin_thumbanail()
show_entry_thumbnail.short_description = 'Argazkia'
show_entry_thumbnail.allow_tags = True


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_es', 'published', 'is_public', show_entry_thumbnail)
    list_display_links = ('id', 'title_es')
    ordering = ('-id',)
    search_fields = ['title_es', 'summary_es']
    prepopulated_fields = {'slug_es': ('title_es',), 'slug_eu': ('title_eu',)}
    photologue_image_fields = ('image',)

    class Media:
        js = (getattr(settings, 'STATIC_URL', '') + 'tiny_mce/tiny_mce.js',
              )


class TinyMCEArticleAdmin(ArticleAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('body_es', 'body_eu'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'theme': "advanced",
                    'mode': "textareas",
                    'plugins': "media",
                    'extended_valid_elements': "iframe[src|width|height|name|align]",
                    'theme_advanced_buttons1': "formatselect,bold,italic,underline,separator,justifyleft,justifycenter,justifyright, justifyfull,bullist,numlist,undo,redo,link,unlink,image,code,removeformat",
                    'theme_advanced_buttons2': "",
                    'theme_advanced_buttons3': "",
                    'theme_advanced_toolbar_location': "top",
                    'theme_advanced_toolbar_align': "left",
                    'theme_advanced_resizing': 'false',
                    'media_strict': 'false',
                },
            ))
        return super(TinyMCEArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Article, TinyMCEArticleAdmin)
