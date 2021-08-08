from django.shortcuts import render, HttpResponseRedirect
from news.models import Category, Post
from django.urls import reverse_lazy
# Create your views here.

category = Category.objects.all()
post = Post.objects.all()

for_main_page = {
    'title': "news",
    "categorys": category,
    'posts': Post.objects.all(),
    'recent': Post.objects.all()[:3],
    'search': False
}

for_post_page = {
    'title': 'News Post',
    'home': 'active',
    'category': Category.objects.all()
}


def main_page(request):
    if request.GET.get('id'):
        for_main_page['posts'] = Post.objects.all().filter(category=request.GET.get('id'))
        for_main_page['active'] = Category.objects.get(id=request.GET.get('id')).category_name
        for_main_page['home'] = ''
    else:
        for_main_page['posts'] = Post.objects.all()
        for_main_page['home'] = 'active'
        for_main_page['active'] = ''

    return render(request, 'news/home.html', for_main_page)


def post(request, id):
    try:
        for_post_page['post'] = Post.objects.get(id=id)
        return render(request, 'news/post.html', for_post_page)
    except:
        return HttpResponseRedirect(reverse_lazy('news:main_page'))

for_new = {
    'categorys': Category.objects.all(),
}
