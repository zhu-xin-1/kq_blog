"""ke_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ke_blog),
    path("ke-blog",views.ke_blog),
    path("user_login",views.user_login),
    path("user_register",views.user_register),
    #url路由分发 通过在app中建立urls文件 ，将normal_user地址分发到normal_user的app中，来使得结构清晰，分工明确
    path("normal_user/",include("normal_user.urls")),

    # 用于创建数据表后添加初始数据 ，初始添加完后可删除
    #path("auu",views.auu),
]
