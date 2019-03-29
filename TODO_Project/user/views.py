# from django.contrib.auth.hashers import make_password, check_password
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse
#
# from user.forms import UserLogin
#
#
# from user.models import User
#
#
# # 登录页面
# # @login_token
# def login(request):
#     """登录"""
#     # get请求返回登录页面
#     if request.method == 'GET':
#         return render(request, 'login.html')
#
#     if request.method == 'POST':
#         data = request.POST
#         form = UserLogin(data)
#         if form.is_valid():
#             # 有用户
#             user = User.objects.filter(username=form.cleaned_data.get('username'))
#             # if check_password(pwd, user.first().password):
#             #     # 验证失败
#             #     return render(request, 'login.html', {'errors': form.errors})
#             if not user:
#                 # 说明密码错误
#                 return render(request, 'login.html', {'errors': form.errors})
#             else:
#                 # cookie+session
#                 request.session['user_id'] = user.first().id
#                 return HttpResponseRedirect(reverse('todo_list:index'))
#         else:
#             return render(request, 'login.html', {'errors': form.errors})
#
#
# def register(request):
#     """注册页面"""
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     if request.method == 'POST':
#         username = request.POST.get('user_name')
#         password = request.POST.get('pwd')
#         password2 = request.POST.get('cpwd')
#         password = make_password(password)
#         if not all([username, password, password2]):
#             mag = '信息不完整'
#             return render(request, 'register.html', {'mag': mag})
#         if User.objects.filter(username=username).first():
#             mag = '该用户已经被注册， 请登录'
#             return render(request, 'register.html', {'mag': mag})
#         # if password != password2:
#         #   mag = '两次密码不一致'
#         #   return render(request, 'register.html', {'mag': mag})
#         User.objects.create(username=username, password=password)
#         return HttpResponseRedirect(reverse('user:login'))
#
#
# # 注销
# def logout(request):
#     """注销"""
#     if request.method == 'GET':
#         request.session.flush()
#         return HttpResponseRedirect(reverse('user:login'))
#
#
#
#
#
#
#
