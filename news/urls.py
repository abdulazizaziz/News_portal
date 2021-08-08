from django.contrib import admin
from django.urls import path, include
from news.views import main_page, post

app_name = "news"

urlpatterns = [
    path('', main_page, name='main_page'),
    path('post/<int:id>/', post, name='post'),
]
