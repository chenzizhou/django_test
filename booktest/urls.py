from django.urls import path

from booktest import views

app_name = 'booktest'  # 命名空间
urlpatterns = [
    path('', views.index),
]
