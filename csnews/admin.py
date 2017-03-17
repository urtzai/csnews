from django.contrib import admin
from csnews.models import Article

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
    list_display = ('id', 'title', 'published', 'is_public', show_entry_thumbnail)
    list_display_links = ('id', 'title')
    ordering = ('-id',)
    search_fields = ['title', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    photologue_image_fields = ('image',)


admin.site.register(Article, ArticleAdmin)
