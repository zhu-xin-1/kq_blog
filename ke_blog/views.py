from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from normal_user import models as md
#登陆首界面
def ke_blog(request):
    return render(request,"base.html")
# 测试一下数据库
def auu(request):
    # 不推荐
    # test=normal_user.models.Authority(authority_degree =1,authorit_query=True,authorit_add = True,
    #                                   authorit_delete = True,authorit_update = True,)
    # test.save()
    # 推荐 使用ORM方式进行操作
    test=md.Authority.objects.create(authority_degree =2,authorit_query=True,authorit_add = False,
                                      authorit_delete = False,authorit_update = False,)

    return HttpResponse("<p>添加成功</p>")

def user_login(request):
    request.encoding = 'utf-8'
    if '注册' in request.POST:
        return render(request, 'user_register.html', {'result': "请填写用户名及密码"})
    print(request.POST)
    if '登陆' in request.POST:
        books = md.normal_user.objects.filter(user_name=request.POST['name'])
        if not books:
            return render(request, 'base.html', {'result': "账号密码错误"})
        elif request.POST['pass'] == books[0].user_password:
            return render(request,'kq_blog.html',{'result':"登陆成功"})

    return HttpResponse('<p>无效</p>')

def user_register(request):
    if "注册" in request.POST:
        test=md.normal_user(user_name=request.POST['name'],user_password=request.POST['pass'])
        test.save()
        return render(request,'base.html',{'result':"注册成功"})
    else:
        return HttpResponse('<p>失败</p>')
    #return HttpResponse('<p>失败</p>')