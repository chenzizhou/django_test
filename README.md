1.创建虚拟环境
python -m venv venv  --Python自带

pip install virtualenv   --第三方包
virtualenv venv

# 激活虚拟环境
# macOS/Linux
source myenv/bin/activate
# Windows
myenv\Scripts\activate
# 退出虚拟环境
deactivate

2.下载django
pip install django -i 镜像 --trusted-host 信任服务器

3、连接mysql数据库模块mysqlclient-下载轮子
https://blog.csdn.net/yanxi32666/article/details/139708115?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522c2958e156be5cbb0691cb04ba6627abc%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=c2958e156be5cbb0691cb04ba6627abc&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-139708115-null-null.142^v102^pc_search_result_base5&utm_term=pycharm%E4%B8%8B%E8%BD%BDmysqlclient&spm=1018.2226.3001.4187

4、创建模型。分析所用表之间的关系，通过orm映射快速创建数据表。在应用模块下models.py中定义。定义完成后需添加在项目容器下setting.py》INSTALLED_APPS中
)1. Django 3.2+ 原生支持（推荐）
直接在模型字段使用`db_comment`参数：
class Article(models.Model):
    title = models.CharField(
        max_length=200,
        db_comment='文章标题，最大长度200字符'
    )
    content = models.TextField(
        db_comment='文章正文内容，支持富文本'
    )

)2. 手动SQL注释（适用于旧版本）
在迁移文件中添加注释操作：
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('your_app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE your_app_article MODIFY COLUMN title VARCHAR(200) COMMENT '文章标题，最大长度200字符';",
            reverse_sql="ALTER TABLE your_app_article MODIFY COLUMN title VARCHAR(200);"
        )
    ]

python manage.py makemigrations # 生成迁移文件
python manage.py sqlmigrate your_app 0002 # 查看SQL语句
python manage.py migrate # 执行迁移
5、创建视图
在应用模块views.py中写处理逻辑

6、创建url
在应用模块urls.py中写路径

5、创建视图
在应用模块views.py中写处理逻辑

6、创建url
在应用模块urls.py中写路径
参考文件：https://blog.csdn.net/weixin_73749601/article/details/146356702?ops_request_misc=%257B%2522request%255Fid%2522%253A%25220dccbf8ffe0c77eb363bf97de2b66082%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=0dccbf8ffe0c77eb363bf97de2b66082&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-146356702-null-null.142^v102^pc_search_result_base5&utm_term=django%E4%BD%BF%E7%94%A8bootstrap%E6%A8%A1%E6%9D%BF&spm=1018.2226.3001.4187

