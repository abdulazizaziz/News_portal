from django.contrib import admin
from django.urls import path
from .views import main_page, delete, edit, update, login, logout, create, category, create_category, delete_category, update_category
from .views import users, create_user, delete_user

app_name = "admin_panel"

urlpatterns = [
    path('', main_page, name="main_page"),
    path('delete/<int:id>/', delete, name="delete"),
    path('edit/<int:id>/', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('create', create, name="create"),


    path('category', category, name="category"),
    path('create_category', create_category, name="create_category"),
    path('delete_category/<int:id>', delete_category, name="delete_category"),
    path('update_category/<int:id>', update_category, name="update_category"),
    path('users', users, name="users"),
    path('create_user', create_user, name="create_user"),
    path('delete_user/<int:id>', delete_user, name="delete_user"),
]