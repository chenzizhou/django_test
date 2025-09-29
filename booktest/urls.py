from django.urls import path

from booktest import views

app_name = 'booktest'  # 命名空间
urlpatterns = [
    path('', views.index, name='index'),
    path('cookie_set/', views.cookie_set, name='cookie_set'),
    path('session_test/', views.session_test, name='session_test'),
    path('create/', views.create, name='create'),
    path('delete<id>/', views.delete, name='delete'),
    path('list<id>/', views.list, name='list'),
    path('json1/', views.json1, name='json1'),
    path('json2/', views.json2, name='json2'),
    path('guolvqi/', views.guolvqi, name='guolvqi'),

]
