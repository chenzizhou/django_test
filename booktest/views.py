from datetime import date
from urllib.parse import quote, unquote

from django.db.models import F, Q, Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from booktest.models import BookInfo, HeroInfo


# Create your views here.

def index(request):
    print(request.session.get('h1'))  # 获取session
    request.session.clear()
    print(request.session.get('h1'), 123)  # 获取session
    # request.session.flush()
    del request.session['h1']
    return HttpResponse("index")


def session_test(request):
    print(request.session.get('h1'))
    print(request.session.session_key)
    # sessionid = request.COOKIES.get('sessionid')  # 获取sessionid
    request.session['h1'] = 'hello1'
    # request.session.set_expiry(5)
    return HttpResponse('写session')


def cookie_set(request):
    value = request.COOKIES.get('h1')
    print(unquote(value))  # 获取Cookie
    response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>")
    # UnicodeEncodeError: 'latin-1' codec can't encode characters in position 204-205: ordinal not in range(256)
    chinese_str = '中文'
    encoded_value = quote(chinese_str)
    response.set_cookie('h1', encoded_value)
    return response


# 查询所有图书并显示
def index(request):
    # list = BookInfo.books.all() #查询所有未删除的用户
    # list = BookInfo.books.filter(id__exact=1)
    # list = BookInfo.books.filter(btitle__contains='传')
    # list = BookInfo.books.filter(btitle__endswith='部')
    # list = BookInfo.books.filter(pk__in=[1, 3, 5])
    # list = BookInfo.books.filter(id__gt=3)
    # list = BookInfo.books.exclude(id=3)
    # list = BookInfo.books.filter(bpub_date__year=1980)
    # list = BookInfo.books.filter(bpub_date__gt=date(1990, 1, 1))
    # list = BookInfo.  books  .filter(btitle__isnull=False)
    # list = BookInfo.books.filter(heroes__hcontent__contains='八')
    # list = BookInfo.books.exclude(id=3)
    # list = BookInfo.objects.all()
    # list = HeroInfo.objects.filter(hbook__btitle='天龙八部')
    # list = BookInfo.books.filter(bread__gte=F('bcommet'))
    # list = BookInfo.books.filter(bread__gt=F('bcommet') * 2)
    # list = BookInfo.books.filter(~Q(pk=3))  # 过滤掉id=3的
    # list = BookInfo.books.aggregate(Sum('bread'))
    list = BookInfo.books.count()
    print(list, '----------------')
    # return render(request, 'booktest/index.htm', {'list': list})
    # return render(request, 'booktest/list.html', {'list': list})
    # return HttpResponse(list['bread__sum'])
    return HttpResponse(list)


# 创建新图书
def create(request):
    book = BookInfo.books.create('流星蝴蝶剑', date(1995, 12, 30))
    book.save()
    # 转向到首页
    return redirect('/booktest')


# 逻辑删除指定编号的图书
def delete(request, id):
    print(id)
    book = BookInfo.objects.get(pk=int(id))
    book.isDelete = True
    book.save()
    # 转向到首页
    return redirect('/booktest')


def list(request):
    list = HeroInfo.objects.filter(hbook__btitle='天龙八部')
    print(list, '--------------------')
    context = {'list': list}
    return render(request, 'booktest/list.html', context)


def json1(request):
    return render(request, 'booktest/json1.html')


def json2(request):
    return JsonResponse({'h1': 'hello', 'h2': 'world'})


def guolvqi(request):
    list = BookInfo.books.all()
    print(list, '----------------')
    # raise Exception('自定义异常')
    return render(request, 'booktest/guolvqi.html', {'list': list})
