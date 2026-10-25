from django.shortcuts import render
from django.urls import reverse
from .models import *
from blog.models import Article


def home(request):
    sliders = Slider.objects.filter(is_active=True).order_by('-order')
    ceo_speech = ManagerSpeech.objects.first()
    
    last_events = Article.objects.filter(article_type=Article.ArticleType.EVENTS, status=Article.Status.PUBLISHED).order_by('-created_at')[:6]
    last_news = Article.objects.filter(article_type=Article.ArticleType.NEWS, status=Article.Status.PUBLISHED).order_by('-created_at')[:6]
    most_news = Article.objects.filter(article_type=Article.ArticleType.NEWS, status=Article.Status.PUBLISHED).order_by('-view_count')[:4]
    galleries = Article.objects.filter(article_type=Article.ArticleType.GALLERIES, status=Article.Status.PUBLISHED).order_by('-created_at')[:6]
    
    context = {
        'sliders': sliders,
        'ceo_speech': ceo_speech,
        'last_events': last_events,
        'last_news': last_news,
        'most_news': most_news,
        'galleries': galleries
    }
    return render(request, 'home/home.html', context)


def about(request):
    breadcrumbs = [
        {
            'title': 'صفحه اصلی',
            'url': reverse('home:home')
        },
        {
            'title': 'درباره ما',
            'url': ''
        }
    ]
    
    context = {
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'home/about.html', context)


def contact(request):
    breadcrumbs = [
            {
                'title': 'صفحه اصلی',
                'url': reverse('home:home')
            },
            {
                'title': 'ارتباط با ما',
                'url': ''
            }
        ]
    
    context = {
        'breadcrumbs': breadcrumbs,
    }
    
    return render(request, 'home/contact.html', context)