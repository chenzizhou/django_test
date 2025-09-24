from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(verbose_name='用户id', primary_key=True,
                               help_text='用户id',
                               db_comment='用户id')  # verbase_name在Django管理后台显示的字段名称，help_text在Django管理后台显示的字段提示信息
    username = models.CharField(max_length=20, unique=True, help_text='用户名')
    password = models.CharField(max_length=20, help_text='密码')
    email = models.EmailField(max_length=50, help_text='邮箱')
    register_date = models.DateTimeField(auto_now_add=True, help_text='注册时间')

    def __str__(self):
        return '%d,%s,%s' % (self.pk, self.username, self.email)  # 定义对象的显示信息，返回一个字符串

    class Meta:
        #     db_table = 'User'  # 设置表名 数据库中会以此显示。默认表名是：应用名_类名 小写
        verbose_name = '用户表'  # 设置对象的名称
        ordering = ['user_id']  # 设置默认排序字段，['-id']表示按照id降序排序
        verbose_name_plural = '用户表'  # 设置对象的复数名称


class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
