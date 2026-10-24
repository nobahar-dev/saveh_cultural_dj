from django.contrib import admin
from .models import *


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active', 'order')
    search_fields = ('title', 'subtitle')
    list_editable = ('is_active', 'order')
    ordering = ('order', '-created_at')