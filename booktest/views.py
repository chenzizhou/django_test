from urllib.parse import quote, unquote

from django.http import HttpResponse


# Create your views here.

def index(request):
    print(request.session.get('h1'))# 获取session
    request.session.clear()
    print(request.session.get('h1'),123)  # 获取session
    # request.session.flush()
    del request.session['h1']
    return HttpResponse("index")



def session_test(request):
    print(request.session.get('h1'))
    print(request.session.session_key)
    sessionid = request.COOKIES.get('sessionid')  # 获取sessionid
    request.session['h1'] = 'hello'
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
