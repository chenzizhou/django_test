"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from app.views import *

# path() 函数接收一个路由模板字符串和一个视图函数作为参数，用于将 URL 路径映射到对应的视图函数。
# re_path() 函数接收一个正则表达式风格的路由模板字符串和一个视图函数作为参数，用于将 URL 路径映射到对应的视图函数。
# re_path(regex, view, kwargs=None, name=None)
# regex：正则表达式字符串，用于匹配 URL。
# view：视图函数或 URL 分发函数（如 include）。
# kwargs：可选参数，传递给视图函数的额外关键字参数。
# name：可选参数，为 URL 模式设置名称，方便在模板中引用。
# urlpatterns = [
#     re_path(r'^article/(?P<id>\d+)/$', views.article_detail, name='article_detail'),
# ]
# 参数 1：路由模板字符串，参数2：视图函数，参数3：路由别名（可选），用于给这个 URL 路由命名，方便在模板或代码中通过 `reverse()` 获取 URL。
# include() 函数用于将一个 URL 路由配置包含到另一个 URL 路由配置中，通常用于模块化 URL 路由配置。
urlpatterns = [
                  re_path('^$', include('booktest.urls', namespace='booktest')),
                  re_path(r'^admin/', admin.site.urls),
                  path('addAccount/', add_account_view, name='addAccount'),
                  path(r'^pic_upload/$', pic_upload),
                  path(r'^pic_handle/$', pic_handle),
                  path('user/', include('user.urls'), name='user'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(urlpatterns, '-----------------------')
