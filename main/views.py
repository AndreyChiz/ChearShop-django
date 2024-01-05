from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories
# Create your views here.
def index(request)-> None:
    context: dict = {
        'title': 'Home - Домашняя',
        'content': 'Магазин мебели HOME',
        'categories': Categories.objects.all()
    }

    return render(request, 'main/index.html', context)


def about(request)-> None:
    context: dict = {
        'title': 'About - О Нас',
        'content': 'О нас',
        'text_on_page': 'Описание магазина'
    }
    return render(request, 'main/about.html', context)


