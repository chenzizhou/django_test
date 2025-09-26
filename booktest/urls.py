from django.urls import path

from booktest import views

app_name = 'booktest'  # 命名空间
urlpatterns = [
    path('index/', views.index, name='index'),
    path('cookie_set/', views.cookie_set, name='cookie_set'),
    path('session_test/', views.session_test, name='session_test'),
]
