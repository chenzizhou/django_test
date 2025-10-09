import hashlib
import random

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        str1 = '%s<br>%s' % (request.path, request.encoding)
        print(str1)
        return render(request, 'user/login.html')
    else:
        # 验证用户凭证
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me', False)
        print(username, password, '---------------')
        user_obj = auth.authenticate(request=request, username=username, password=password)
        if not user_obj:
            return render(request, 'user/login.html', {'errorMessage': '用户名或密码错误'})
        else:

            auth.login(request, user_obj)
            path = request.GET.get("next") or "/user/index/"
            print(path, '--------------------')
            return redirect(path)
        response = redirect(reverse("user:index"))

        # 生成随机令牌
        token = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
        response.set_cookie(
            'remember_token',
            token,
            max_age=14 * 24 * 60 * 60,  # 14天
            secure=True,  # 只在HTTPS下发送
            httponly=True,  # 防止XSS攻击
            samesite='Lax')  # 防止CSRF攻击

        # user = authenticate(request, username=username, password=password)
        # user = User.objects.filter(username=username, password=password).first()
        # if user is not None:
        #     # 登录用户
        #     # login(request, user)
        #
        #     # 如果用户选择了“记住我”，设置cookie
        #     if remember_me:
        #         # 生成随机令牌
        #         token = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
        #         # 设置cookie，有效期为14天
        #         response = HttpResponseRedirect('/')
        #         response.set_cookie(
        #             'remember_token',
        #             token,
        #             max_age=14 * 24 * 60 * 60,  # 14天
        #             secure=True,  # 只在HTTPS下发送
        #             httponly=True,  # 防止XSS攻击
        #             samesite='Lax'  # 防止CSRF攻击
        #         )
        return response

        # 没有选择“记住我”，直接登录
    # 如果登录失败，返回登录页


def register_view(request):
    u = User(username='nature', password='nature')
    u.save()
    return HttpResponse("注册成功")


def index(request):
    print(request.user.is_authenticated)
    return HttpResponse("登录成功")


def toRegister(request):
    return render(request, 'user/register.html')


@require_http_methods(['POST'])
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    pwd1 = request.POST.get('pwd1')
    if password == pwd1:
        # User.objects.create(username=username, password=password)
        User.objects.create_user(username=username, password=password)
        return redirect(reverse("user:login"))
    else:
        return render(request, 'user/register.html', {'errorMessage': '两次密码不一致'})
