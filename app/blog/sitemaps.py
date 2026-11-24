from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    
    def items(self):
        return Article.objects.filter(status=Article.Status.PUBLISHED)
    
    def lastmod(self, obj):
        return obj.updated_at
    
    
class StaticViewsSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
    
    def items(self):
        return ['home:home', 'home:about', 'home:contact', 'home:urban']
    
    def location(self, item):
        return reverse(item)