from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелина Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': True},
    {'id': 3, 'title': 'Джуля Робертс', 'content': 'Биография Джуля Робертс', 'is_published': True},
]


menu = ["О сайте", "Добавьте статью", "Обратная связь", "Войти"]


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport', ))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


