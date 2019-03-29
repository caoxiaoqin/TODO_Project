from django.shortcuts import render, redirect
from todo_list.models import TodoList


def home(request):
    if request.method == 'POST':
        if request.POST['待办事项'] == '':
            content = {'全部清单': TodoList.objects.all(), '警告': '请输入内容！'}
            return render(request, "home.html", content)
        else:
            a_row = TodoList(thing=request.POST['待办事项'])
            a_row.save()
            content = {'全部清单': TodoList.objects.all(), '信息': '添加成功！'}
            return render(request, "home.html", content)
    elif request.method == 'GET':
        content = {'全部清单': TodoList.objects.all()}
        return render(request, "home.html", content)  # 渲染出一个逻辑，返回给用户


def about(request):
    return render(request, 'about.html')  # 渲染出一个逻辑，返回给用户


def edit(request):
    return render(request, 'edit.html')  # 渲染出一个逻辑，返回给用户


def newedit(request, 每一件事_id):
    if request.method == 'POST':
        if request.POST['已修改事项'] == '':
            return render(request, 'newedit.html', {'警告': '请输入内容！'})
        else:
            a = TodoList.objects.get(id=每一件事_id)
            a.thing = request.POST['已修改事项']
            a.save()
            return redirect("todo_list:主页")
    elif request.method == 'GET':
        content1 = {'待修改事项': TodoList.objects.get(id=每一件事_id).thing}
        return render(request, 'newedit.html', content1)  # 渲染出一个逻辑，返回给用户


def delete(request, 每一件事_id):  # 完成删除的逻辑处理，然后再把网页跳转到主页
    # 先要知道用户点的那个条记录，然后再删
    # 利用forloot_counter，从1开始计数的
    a = TodoList.objects.get(id=每一件事_id)
    a.delete()
    return redirect("todo_list:主页")


def cross(request, 每一件事_id):  # 完成划掉的逻辑处理，然后再把网页跳转到主页
    if request.POST['完成状态'] == '已完成':
        a = TodoList.objects.get(id=每一件事_id)
        a.done = True
        a.save()
        return redirect("todo_list:主页")
    else:
        a = TodoList.objects.get(id=每一件事_id)
        a.done = False
        a.save()
        return redirect("todo_list:主页")

#
# def index(request):
#     if request.method == 'GET':
#         return render(request, 'index.html')
#
