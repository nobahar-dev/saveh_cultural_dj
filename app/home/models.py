from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


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
    
    
class ManagerSpeech(models.Model):
    title = models.CharField(max_length=250, default='سخن مدیر', verbose_name='عنوان')
    message = CKEditor5Field(default='متن سخن مدیر', verbose_name='سخن مدیر', config_name='default')
    slogan = models.CharField(max_length=400, default='شعار سازمان', verbose_name='شعار سازمان')
    ceo_name = models.CharField(max_length=250, default='رضا یزدی', verbose_name='نام مدیرعامل')
    image = models.ImageField(upload_to='manager/', verbose_name='تصویر مدیر')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        pass
    
    class Meta:
        verbose_name = 'سخن مدیر'
        verbose_name_plural = 'سخن مدیر'
        
        
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=15, verbose_name='شماره تماس')
    message = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
    
    class Meta:
        verbose_name = 'پیام ارتباط با ما'
        verbose_name_plural = 'پیام های ارتباط با ما'
        ordering = ('-created_at', )
        
    def __str__(self):
        return f"{self.full_name} - {self.phone}"