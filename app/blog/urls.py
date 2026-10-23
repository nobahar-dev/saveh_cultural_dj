from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.blog, name='blog'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]
