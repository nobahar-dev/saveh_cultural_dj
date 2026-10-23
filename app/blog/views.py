from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *


def blog(request):
    selected_type = request.GET.get('type', 'all')
    
    articles = Article.objects.filter(status=Article.Status.PUBLISHED)
    
    if selected_type in [Article.ArticleType.NEWS, Article.ArticleType.GALLERIES, Article.ArticleType.EVENTS]:
        articles = articles.filter(article_type=selected_type)
    else:
        selected_type = 'all'
        
    articles = articles.order_by('-created_at')
    paginator = Paginator(articles, 9)
    article_page_obj = paginator.get_page(request.GET.get('page'))
    
    last_news = Article.objects.filter(article_type=Article.ArticleType.NEWS, status=Article.Status.PUBLISHED).order_by('-created_at')[:4]
    last_events = Article.objects.filter(article_type=Article.ArticleType.EVENTS, status=Article.Status.PUBLISHED).order_by('-created_at')[:4]
    
    breadcrumbs_titles = {
        'all': 'اخبار و رویدادها',
        'news': 'آخرین اخبار',
        'events': 'آخرین رویدادها',
        'galleries': 'گزارشات تصویری'
    }
    
    context = {
        'article_page_obj': article_page_obj,
        'selected_type': selected_type,
        'last_news': last_news,
        'last_events': last_events,
        'breadcrumbs': [
            {
                'title': 'صفحه اصلی',
                'url': reverse("home:home")
            },
            {
                'title': breadcrumbs_titles[selected_type],
                'url': ''
            },
        ],
    }
    
    return render(request, 'blog/blog.html', context)


def article_detail(request, slug):
    return render(request, 'blog/detail.html')