from django.contrib import admin
from news.models import Post, Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)