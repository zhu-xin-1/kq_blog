from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
import normal_user
def ke_blog(request):
    return render(request,"base.html")

def user_login(request):
    request.encoding = 'utf-8'
    print(request.POST)
    if '注册' in request.POST:
        return render(request, 'user_register.html', {'result': "请填写用户名及密码"})
    if request.POST['name'] == 'keqiang' and request.POST['pass'] == '123456':
        return render(request,'homepage.html',{'result':"登陆成功"})
    else:
        return render(request,'base.html',{'result':"账户或者密码错误"})

def user_register(request):
    if "注册" in request.POST:
        test=normal_user.models.normal_user(user_name=request.POST['name'],user_password=request.POST['pass'])
        test.save()
        return HttpResponse('<p>注册完成</p>')
    else:
        return HttpResponse('<p>失败</p>')