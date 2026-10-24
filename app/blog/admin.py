from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', )
    prepopulated_fields = {"slug": ('title', )}
    
    
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1
    
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'categories', )
    search_fields = ('title', 'summary', 'content')
    filter_horizontal = ('categories', )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title', )}
    inlines = [ArticleImageInline]
    
    
@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('article', 'caption')
    list_filter = ('article', )
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'article', 'created_at', 'is_approved')
    search_fields = ('full_name', 'created_at', 'article__title')
    list_editable = ('is_approved', )
    ordering = ('-created_at', )