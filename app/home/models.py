from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    subtitle = models.CharField(max_length=400, blank=True, verbose_name='زیر عنوان')
    image = models.ImageField(upload_to='sliders/', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=False, verbose_name='فعال؟')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    
    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'
        ordering = ['order', '-created_at']
        
    def __str__(self):
        return self.title