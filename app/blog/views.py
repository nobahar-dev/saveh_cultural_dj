from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def blog(request):
    articles = Article.objects.filter(article_type=Article.ArticleType.NEWS, status=Article.Status.PUBLISHED).order_by('-created_at')
    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    article_page_obj = paginator.get_page(page_number)
    context = {'article_page_obj': article_page_obj}
    return render(request, 'blog/blog.html', context)