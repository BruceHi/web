from django.db import models

# Create your models here.
# 图书 or 电影


class Type(models.Model):
    id = models.AutoField(primary_key=True)  # Django会自动创建,并设置为主键
    typename = models.CharField(max_length=20)


# 建表名称：myapp_person 这里是 index_name
class Name(models.Model):
    # id 自动创建
    # 虽然这里没有写 id，但是 仍然可以使用 Name.objects.all()[0].id 显示出 id 的索引。
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=10)
