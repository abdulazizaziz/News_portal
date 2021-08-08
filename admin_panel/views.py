from django.shortcuts import render, HttpResponseRedirect
from news.models import Post, Category
from django.urls import reverse_lazy
from .models import Users

# Create your views here.


# login and logout pages
# controling with sesssions

for_login_page = {
    'title': "LOGIN"
}

def login(request):
    if request.method == "POST":
        Puser = request.POST.get('user')
        password = request.POST.get('password')
        # users = Users.objects.all()
        # print('user: ', Puser)
        # print('password: ', password)
        # print(len(users))
        for user in Users.objects.all():
            print(user.user)
            print(user.password)
            if Puser == user.user and password == user.password:
                request.session['admin_id'] = user.id
                request.session['admin'] = user.name
                request.session['role'] = user.role
                request.session['same'] = False
                return HttpResponseRedirect(reverse_lazy('admin_panel:main_page'))
        else:
            for_login_page['wrong'] = "wrong"
            return render(request, "admin_panel/login.html", for_login_page)
    for_login_page['wrong'] = False
    return render(request, "admin_panel/login.html", for_login_page)

def logout(request):
    request.session['admin'] = False
    return HttpResponseRedirect(reverse_lazy('admin_panel:login'))





# post pages view or controller

for_main_page = {
    'title': "Post",
}

def main_page(request):
    if request.session['admin']:
        for_main_page['user'] = request.session['admin']
        for_main_page['role'] = request.session['role']
        for_main_page['posts'] = Post.objects.all()
        return render(request, 'admin_panel/post.html', for_main_page)
    else:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))


def delete(request, id):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        if request.session['admin']:
            post = Post.objects.get(id=id)
            category = Category.objects.get(id=post.category.id)
            category.category_post -= 1
            category.save()
            post.delete()
        return HttpResponseRedirect(reverse_lazy('admin_panel:main_page'))


def edit(request, id):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        post = Post.objects.get(id=id)
        category = Category.objects.all()
        return render(request, 'admin_panel/edit.html', {'post': post, 'categorys': category, "title": "EDIT", 'user': request.session['admin']})


def update(request, id):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        post = Post.objects.get(id=id)

        category = Category.objects.get(id=post.category.id)
        category.category_post -= 1
        category.save()

        category = Category.objects.get(id=int(request.POST.get('category')))
        category.category_post += 1
        category.save()

        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.category = category
        if request.POST.get('img') != "":
            post.img = request.FILES['img']
        post.save()

        return HttpResponseRedirect(reverse_lazy('admin_panel:main_page'))


for_create_page = {
    'title': "Create",
}

def create(request):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        for_create_page['user'] = request.session['admin']
        for_create_page['role'] = request.session['role']
        for_create_page['categorys'] = Category.objects.all()
        if request.method == 'POST' and request.FILES['img']:
            title = request.POST.get('title')
            description = request.POST.get('description').strip()
            category = int(request.POST.get('category'))
            img = request.FILES['img']
            author = Users.objects.get(id=request.session['admin_id'])


            category_inc = Category.objects.get(id=category)
            category_inc.category_post += 1
            category_inc.save()
            news = Post.objects.create(title=title, description=description, category=Category.objects.get(id=category), img=img, author=author)
            news.save()
            return HttpResponseRedirect(reverse_lazy('admin_panel:main_page'))
        
        return render(request, "admin_panel/create.html", for_create_page)




# Category pages view and controller 

for_category_page = {
    'title': "Category",
}
def category(request):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        for_category_page['user'] = request.session['admin']
        for_category_page['role'] = request.session['role']
        for_category_page['categorys'] = Category.objects.all()
        return render(request, "admin_panel/category.html", for_category_page)



def create_category(request):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        if request.method == 'POST':
            name = request.POST.get('category')
            category = Category.objects.create(category_name=name, category_post=0)
            category.save()
            return HttpResponseRedirect(reverse_lazy('admin_panel:category'))
        return render(request, "admin_panel/create_category.html", {'title': 'Create Category', "user": request.session['admin'], 'role': request.session['role']})

def delete_category(request, id):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        category = Category.objects.get(id=id)
        category.delete()

        return HttpResponseRedirect(reverse_lazy('admin_panel:category'))


def update_category(request, id):
    category = Category.objects.get(id=id)
    if request.method != 'POST':
        return render(request, 'admin_panel/update_category.html', {'category': category})
    
    category_name = request.POST.get('category')
    category.category_name = category_name
    category.save()
    return HttpResponseRedirect(reverse_lazy('admin_panel:category'))



# User pages View file and controller

def users(request):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        if request.session['role'] == 1:
            user_page = {
                'title': "Users",
                'user': request.session['admin'],
                'role': request.session['role'],
                'admin_id': request.session['admin_id'],
                'users': Users.objects.all()
            }
            return render(request, "admin_panel/users.html", user_page)
        else:
            return HttpResponseRedirect(reverse_lazy('admin_panel:main_page'))

def create_user(request):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        if request.session['role'] == 1:
            if request.method == 'POST':
                name = request.POST.get('name').strip()
                user = request.POST.get('user').strip()
                password = request.POST.get('password')
                role = request.POST.get('role')

                if Users.objects.filter(user=user):
                    request.session['same'] = True
                    return HttpResponseRedirect(reverse_lazy('admin_panel:create_user'))

                users = Users.objects.create(name=name, user=user, password=password, role=role)
                users.save()
                return HttpResponseRedirect(reverse_lazy('admin_panel:users'))
            user_page = {
                'title': "Add User",
                'user': request.session['admin'],
                'role': request.session['role'],
                'same': False
            }
            if request.session['same']:
                user_page['same'] = True
                request.session['same'] = False
            return render(request, 'admin_panel/create_user.html', user_page)
        else:
            return HttpResponseRedirect(reverse_lazy('admin_panel:main_page'))

def delete_user(request, id):
    if not request.session['admin']:
        return HttpResponseRedirect(reverse_lazy('admin_panel:login'))
    else:
        if request.session['role'] == 1:
            user = Users.objects.get(id=id)
            user.delete()
            return HttpResponseRedirect(reverse_lazy('admin_panel:users'))
        else:
            return HttpResponseRedirect(reverse_lazy('admin_panel:main_page'))