from django.db import models

# Create your models here.
# 最开始从单表开始创立，现在应用多表，并进行多表查询
class normal_user(models.Model):
    # 这里面包含常见的数据类型
    #CharField IntegerField  SmallIntegerField BooleanField DateField
    #字符型        整形              小整形            布尔型      日期型
    #ManyToManyField ForeignKey OneToOneField
    #多对多外键          外键      一对一外键
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_sudent_id = models.ManyToManyField("Student_detail",null=True, blank=True)
    user_authority = models.ForeignKey("Authority", on_delete=models.CASCADE,null=True, blank=True)
class Authority(models.Model):
    authority_degree = models.SmallIntegerField(null=True, blank=True)
    authorit_query=models.BooleanField(null=True, blank=True)
    authorit_add = models.BooleanField(null=True, blank=True)
    authorit_delete = models.BooleanField(null=True, blank=True)
    authorit_update = models.BooleanField(null=True, blank=True)

class Student_detail(models.Model):
    name=models.CharField(max_length=4)
    age = models.SmallIntegerField()
    height = models.SmallIntegerField()
    weigth = models.SmallIntegerField()
    class_id = models.ForeignKey("Sudent_class", on_delete=models.CASCADE,null=True, blank=True)

class Sudent_class(models.Model):
    teach = models.CharField(max_length=4)
    students_number = models.SmallIntegerField()