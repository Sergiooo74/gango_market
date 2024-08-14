from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def root(request):
    return render(request, template_name='market/index.html')

def index(request):
    return render(request, template_name='market/index.html')

def about(request):
    context = {
        "name": "Dmitri",
        "lastname": "Gorin",
        "email": "d.gorin@yandex.ru",
        "title": "About site"
    }
    return render(request, template_name='market/about.html', context=context)

def contacts(request):
    return render(request, template_name='market/contacts.html')

