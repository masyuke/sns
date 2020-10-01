from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from .models import SnsModel, Comment, TodoModel
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.http.response import JsonResponse

# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return redirect('/')
    return render(request, 'signup.html', {'some':100})
  
def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def detailfunc(request, pk):
    object = SnsModel.objects.get(pk=pk)
    comment_list = Comment.objects.filter(article=object)
    if request.method == "POST":
        # データベースに投稿されたコメントを保存
        comment_list.create(text=request.POST["text"],article=object)
    return render(request, 'detail.html', {'object':object, 'article':comment_list })

@login_required
def goodfunc(request, pk):
    post = SnsModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

@login_required
def readfunc(request, pk):
    post = SnsModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read = post.read + 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')

class SnsCreate(CreateView):
    template_name = 'create.html'
    model = SnsModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')

@login_required
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

class TodoList(ListView):
    template_name = 'todo.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'show.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create-todo.html'
    model = TodoModel
    fields =('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todo')

class TodoDelete(DeleteView):
    template_name = 'delete-todo.html'
    model = TodoModel
    success_url = reverse_lazy('todo')

class TodoUpdate(UpdateView):
    template_name = 'update-todo.html'
    model = TodoModel
    fields =('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todo')

def mypagefunc(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = user.snsmodel_set.all()
    return render(request, 'my_page.html', {'user': user, 'posts': posts})
    
