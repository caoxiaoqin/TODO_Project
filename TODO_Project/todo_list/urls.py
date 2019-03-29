# encoding: utf-8
"""
@author: 曹晓芹

"""
from django.urls import path

from todo_list import views


app_name = 'todo_list'
urlpatterns = [
    path('home/', views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('edit/', views.edit, name='编辑'),
    path('delete/<每一件事_id>', views.delete, name='删除'),
    path('cross/<每一件事_id>', views.cross, name='划掉'),
    path('newedit/<每一件事_id>', views.newedit, name='新编辑'),
    # path('index/', views.index, name='index'),

]
