from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from app.models import User, Account

# Create your views here.
app_name = 'app'


def index_view(request):
    return HttpResponse("Hello, world!")


def login_view(request):
    str = '%s<br>%s' % (request.path, request.encoding)
    print(str)
    return render(request, 'app/login.html')


def register_view(request):
    u = User(username='nature', password='nature')
    u.save()
    return HttpResponse("注册成功")


def pic_upload(request):
    return render(request, 'app/pic_upload.html')


def add_account_view(request):
    u = User.objects.get(pk=1)
    a = Account(user=u, account='c60068129', password='Czr1234567890.')
    a.save()
    return HttpResponse("添加账号成功")

def pic_handle(request):
    f1=request.FILES.get('pic')
    print(f1.name)
    fname='%s\\app\\%s'%(settings.MEDIA_ROOT,f1.name)
    with open(fname,'wb') as pic:
        for c in f1.chunks(): #将文件内容写入服务器
            pic.write(c)
    return HttpResponse('OK')
