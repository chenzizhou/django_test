import hashlib
import time
from random import random

from django.contrib.auth.context_processors import auth
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# class User(models.Model):
#     user_id = models.BigAutoField(verbose_name='用户id', primary_key=True,
#                                   help_text='用户id',
#                                   db_comment='用户id')  # verbase_name在Django管理后台显示的字段名称，help_text在Django管理后台显示的字段提示信息
#     username = models.CharField(max_length=20, unique=True, help_text='用户名')
#     password = models.CharField(max_length=20, help_text='密码')
#     email = models.EmailField(max_length=50, help_text='邮箱')
#     register_date = models.DateTimeField(auto_now_add=True, help_text='注册时间')
#
#     def __str__(self):
#         return '%d,%s,%s' % (self.pk, self.username, self.email)  # 定义对象的显示信息，返回一个字符串
#
#     class Meta:
#         #     db_table = 'User'  # 设置表名 数据库中会以此显示。默认表名是：应用名_类名 小写
#         verbose_name = '用户表'  # 设置对象的名称
#         ordering = ['user_id']  # 设置默认排序字段，['-id']表示按照id降序排序
#         verbose_name_plural = '用户表'  # 设置对象的复数名称


class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


class RememberToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remember_tokens')
    token = models.CharField(max_length=64)
    expires = models.IntegerField()  # 存储Unix时间戳

    def save(self, *args, **kwargs):
        if not self.token:
            # 生成随机token
            self.token = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
        if not self.expires:
            # 设置默认过期时间为14天后
            self.expires = time.time() + 14 * 24 * 60 * 60
        super().save(*args, **kwargs)


class Account(models.Model):
    account_id = models.BigAutoField(primary_key=True)
    account = models.CharField(max_length=20, unique=True, )
    password = models.CharField(max_length=20, )
    platform = models.CharField(max_length=20, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', )

    def __str__(self):
        return '%d' % (self.account_id)

    class Meta:
        verbose_name = '账号表'  # 设置对象的名称
