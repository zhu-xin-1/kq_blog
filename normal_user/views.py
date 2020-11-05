from django.shortcuts import render
from normal_user.models import normal_user, Authority
from django.http import HttpResponse
# Create your views here.
def add_user(request):
    test = Authority.objects.create(authority_degree=2, authorit_query=True, authorit_add=False,
                                       authorit_delete=False, authorit_update=False, )
    return HttpResponse('<p>添加成功</p>')


import random

print(random.randint(0, 9))
#用于数据操作
def date_squery(request):
    # ORM方式 表名.objects.查询语句[?].列名 就是需要查询的数据
    # all() 查询表的全部内容相当于SELECT * FROM XXX
    # 其中pk是主键的意思，一般来说是ID
    # filter() 相当于 SELECT * FROM XXX WHERE XXX
    # exclude() ,与filter共用，一个返回选取的，一个返回未选取的
    # filter 和exclude 可以用__的方式进行模糊查询 ，比如查询价格在[100,200]之间的数据 ，就可以用filter(price__in=[100,200])
    #       还有一些其他的__关键字, gt是>，gte是>=,lt是<,lte是<=,range是闭区间，contain是包含（title__contain="菜“）则是查询标题中有菜的行
    #       icontain 是不区分大小写的包含，xx__startswith="菜"是开头字符串未菜的数据，endswith同上
    #       year必须是日期数据DateField时才能使用。month,day同理
    # get() ,获取符合条件的单独的对象 ，只能有一个
    # order_by() 对查询结果进行排序 reverse()对查询结果进行反转 ，比如order_by("xxx").reverse()
    # count() 用于对查询结果计数 比如用于filter(pk=1).count() 返回整数
    # first() 返回第一条数据 last()返回最后一条数据
    # exist() 用于判断数据是否存在
    # values("xxx","xxx") 用于返回数据的特定列  ，并且返回的是字典，可根据列名查询值
    # distinct() 对以查询的数据进行去重，一般结合values或者values_list()
    # delete() ,可直接查询数据中 .delete() 即可删除
    #  update(),同上 不过需要在括号中增加需要修改的值 键=值
    # test = normal_user.objects.order_by("user_name")
    # print(test[0].user_name)
    return HttpResponse("<p>查询成功</p>")