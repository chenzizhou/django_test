from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    # class Meta:
    #     db_table = 'User'  # 设置表名


class Account(models.Model):
    account = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    platform = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
