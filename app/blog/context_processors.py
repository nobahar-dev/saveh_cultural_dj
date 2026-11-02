from .models import Article


def footer_latest_news(request):
    footer_latest_news = Article.objects.filter(article_type=Article.ArticleType.NEWS, status=Article.Status.PUBLISHED).order_by('-created_at')[:3]
    context = {
        'footer_latest_news': footer_latest_news,
    }
    return context