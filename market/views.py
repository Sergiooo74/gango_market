from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import PostForm
from .models import Post

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


def add_post(request):
    if request.method == "GET":
        form = PostForm()
        context = {
            'form': form,
            'title': 'Post adding'
        }
        return render(request, template_name='market/add_post.html', context=context)

    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = Post()
            post.author = form.cleaned_data['author']
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.save()

            return index(request)


def post_list(request):
    posts = Post.objects.all()
    context = {
        'title': 'Posts',
        'posts': posts
    }
    return render(request, template_name='market/posts.html', context=context)