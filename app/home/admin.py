from django.contrib import admin
from .models import *


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active', 'order')
    search_fields = ('title', 'subtitle')
    list_editable = ('is_active', 'order')
    ordering = ('order', '-created_at')
    
    
@admin.register(ManagerSpeech)
class ManagerSpeechAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    
    def has_add_permission(self, request):
        return not ManagerSpeech.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_view_permission(self, request, obj=None):
        return True
    
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('full_name', 'phone')
    ordering = ('-created_at', )
    readonly_fields = ('created_at', )