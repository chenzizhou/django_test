from django.http import HttpResponse
from django.shortcuts import render

from app.models import User

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
