from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, SnsCreate, TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate, mypagefunc
from . import views
urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', SnsCreate.as_view(), name='create'),
    path('', views.index, name='index'),
    path('todo/', TodoList.as_view(), name='todo'),
    path('show/<int:pk>', TodoDetail.as_view(), name='show'),
    path('create-todo/', TodoCreate.as_view(), name='create-todo'),
    path('delete-todo/<int:pk>', TodoDelete.as_view(), name='delete-todo'),
    path('update-todo/<int:pk>', TodoUpdate.as_view(), name='update-todo'),
    path('my_page/<int:user_id>', mypagefunc, name='my_page'),
]