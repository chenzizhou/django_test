from django.urls import path

from user.views import login_view, index, toRegister, register

app_name = 'user'

urlpatterns = [
    path('toLogin/', login_view, name='toLogin'),
    path('login/', login_view, name='login'),
    path('toRegister/', toRegister, name='toRegister'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
]
