from django.urls import path
from .views import index, about, contacts, add_post, post_list

app_name = 'market'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('post/add/', add_post, name='add_post'),
    path('post/', post_list, name='post_list'),
]