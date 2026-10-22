from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "پیش نویس"
        PUBLISHED = "published", "منتشر شده"
        
    class ArticleType(models.TextChoices):
        NEWS = "news", "آخرین اخبار"
        EVENTS = "events", "آخرین رویدادها"
        GALLERIES = "galleries", "گالری تصاویر"
    
    title = models.CharField(max_length=250, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=280, unique=True, blank=True, allow_unicode=True, verbose_name='شناسه آدرس')
    summary = models.CharField(max_length=500, verbose_name='خلاصه مقاله')
    content = models.TextField(verbose_name='متن مقاله')
    featured_image = models.ImageField(upload_to='blog/featured', verbose_name='تصویر شاخص')
    article_type = models.CharField(max_length=10, choices=ArticleType.choices, default=ArticleType.NEWS, verbose_name="نوع مقاله")
    categories = models.ManyToManyField('Category', related_name='articles', verbose_name='دسته بندی ها')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='articles', verbose_name='نویسنده')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT, verbose_name='وضعیت انتشار')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین ویرایش")
    meta_descriptions = models.CharField(max_length=180, blank=True, verbose_name="توضیحات سئو")
    view_count = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-created_at"]
        
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title, allow_unicode=True)
            candidate = base_slug
            counter = 1
            
            while Article.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                counter += 1
                candidate = f"{base_slug}-{counter}"
                
            self.slug = candidate
            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, verbose_name="شناسه آدرس")
    descriptions = models.TextField(blank=True, verbose_name="توضیحات دسته بندی")
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    
class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='gallery_images', verbose_name="مقاله")
    image = models.ImageField(upload_to="blog/gallery", verbose_name="تصویر گالری")
    alt_text = models.CharField(max_length=250, blank=True, verbose_name="متن جایگزین تصویر")
    caption = models.CharField(max_length=250, blank=True, verbose_name="توضیح تصویر")
    order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")
    
    class Meta:
        verbose_name = "تصویر گالری"
        verbose_name_plural = "تصاویر گالری"
        ordering = ['order', 'id']
        
    def __str__(self):
        return f"{self.article.title} - تصویر {self.pk}"