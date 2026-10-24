from django.shortcuts import render
from django.urls import reverse


def home(request):
    return render(request, 'home/home.html')


def about(request):
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
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'home/about.html', context)


def contact(request):
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
    }
    
    return render(request, 'home/contact.html', context)