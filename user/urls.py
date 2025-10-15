from django.urls import path

from user.views import login_view, index, toRegister, register, home, toAccount, AddAccount, modAccount, delAccount, \
    logout

app_name = 'user'

urlpatterns = [
    path('toLogin/', login_view, name='toLogin'),
    path('login/', login_view, name='login'),
    path('toRegister/', toRegister, name='toRegister'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('toAccount/', toAccount, name='toAccount'),
    path('AddAccount/', AddAccount, name='AddAccount'),
    path('modAccount/', modAccount, name='modAccount'),
    path('delAccount/<int:account_id>/', delAccount, name='delAccount'),
    path('logout', logout, name='logout'),
]
