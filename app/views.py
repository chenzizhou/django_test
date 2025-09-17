from django.http import HttpResponse
from django.shortcuts import render

from app.models import User, Account

# Create your views here.
app_name = 'app'


def index_view(request):
    return HttpResponse("Hello, world!")


def login_view(request):
    return HttpResponse("登录界面")


def register_view(request):
    u = User(username='nature', password='nature')
    u.save()
    return HttpResponse("注册成功")


def add_account_view(request):
    u = User.objects.get(pk=1)
    a = Account(user=u, account='c60068129', password='Czr1234567890.')
    a.save()
    return  HttpResponse("添加账号成功")
