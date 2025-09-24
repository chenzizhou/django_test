from django.http import HttpResponse
from django.shortcuts import render

from user.models import User


# Create your views here.
def login_view(request):
    str = '%s<br>%s' % (request.path, request.encoding)
    print(str)
    return render(request, 'app/login.html')


def register_view(request):
    u = User(username='nature', password='nature')
    u.save()
    return HttpResponse("注册成功")
