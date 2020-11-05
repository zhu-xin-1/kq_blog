from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("add_user/",views.add_user),
    path("date_squery/",views.date_squery),
    # 用于创建数据表后添加初始数据 ，初始添加完后可删除
    #path("auu",views.auu),
]