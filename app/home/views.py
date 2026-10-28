from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
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
    ceo_speech = ManagerSpeech.objects.first()
    
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
        'breadcrumbs': breadcrumbs,
        'ceo_speech': ceo_speech
    }
    return render(request, 'home/about.html', context)


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'پیام شما ارسال شد')
            return redirect('home:contact')
        else:
            print(contact_form.errors)
            messages.error(request, "ارسال اطلاعات به درستی انجام نشده است")
    else:
        contact_form = ContactForm()
    
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
        'contact_form': contact_form
    }
    
    return render(request, 'home/contact.html', context)