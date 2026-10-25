from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import F
from .models import *
from .forms import *


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
    article = get_object_or_404(Article, slug=slug, status=Article.Status.PUBLISHED)
    article_gallery = ArticleImage.objects.filter(article=article).order_by('-order')
    comments = Comment.objects.filter(article=article, is_approved=True)
    last_news = Article.objects.filter(article_type=Article.ArticleType.NEWS, status=Article.Status.PUBLISHED).order_by('-created_at')[:4]
    last_events = Article.objects.filter(article_type=Article.ArticleType.EVENTS, status=Article.Status.PUBLISHED).order_by('-created_at')[:4]
    
    # view count
    session_key = f"viewed_article_{article.pk}"
    if not request.session.get(session_key):
        Article.objects.filter(pk=article.pk).update(view_count=F('view_count') + 1 )
        request.session[session_key] = True
        
    article.refresh_from_db(fields=['view_count'])
    
    # comment form
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.is_approved = False
            comment.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد و پس از تایید نمایش داده می شود.')
            return redirect('blog:article_detail', slug=article.slug)
    else:
        comment_form = CommentForm()
    
    type_info = {
        Article.ArticleType.NEWS: {
            'title': 'آخرین اخبار',
            'type': 'news'
        },
        Article.ArticleType.EVENTS: {
            'title': 'آخرین رویدادها',
            'type': 'events'
        },
        Article.ArticleType.GALLERIES: {
            'title': 'گزارشات تصویری',
            'type': 'galleries'
        }
    }
    
    article_info = type_info.get(article.ArticleType, {
        'title': 'آخرین اخبار و رویدادها',
        'type': 'all'
    })
    
    breadcrumbs = [
        {
            'title': 'صفحه اصلی',
            'url': reverse('home:home')
        },
        {
            'title': article_info['title'],
            'url': reverse('blog:blog') + '?type=' + article_info['type']
        },
        {
            'title': article.title,
            'url': ''
        }
    ]
    
    context = {
        'article': article,
        'article_gallery': article_gallery,
        'comments': comments,
        'last_news': last_news,
        'last_events': last_events,
        'breadcrumbs': breadcrumbs,
        'comment_form': comment_form
    }
    return render(request, 'blog/detail.html', context)