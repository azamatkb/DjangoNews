from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)