from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer', 'project', 'created_at']
    list_filter = ['project']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'like', 'hits']

admin.site.register(Article, ArticleAdmin)
