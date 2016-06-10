#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import  HttpResponse,render
from app01 import  models
from  app01.forms  import   forign  as ForignForm
def create_user_group(request):
    models.UserGroup_New.objects.create(caption='CTO')
    models.UserGroup_New.objects.create(caption='CEO')
    models.UserGroup_New.objects.create(caption='COO')
    return HttpResponse('ok')

def  create_user(request):
    obj = ForignForm.UserForm(request.POST)
    if  request.method == 'POST':
        if obj.is_valid():
            all_data = obj.clean()
            print all_data
            # group_obj = models.UserGroup_New.objects.get(id=all_data['user_group'])
            # models.User_New.objects.create(username=all_data['username']
            #                                ,user_group=group_obj)
            #这种方式是对象获取数据，user_group是对象，要接收对象赋值，下面是数值赋值，数据库级别字段操作
            # models.User_New.objects.create(username=all_data['username']
                                            # ,user_group_id=all_data['user_group'])   第二种方法
            models.User_New.objects.create(**all_data)
            print   models.User_New.objects.all().count()
        else:
            print "novalied"
    # user_list = models.User_New.objects.all()
    # val = request.GET['username']
    # user_list = models.User_New.objects.filter(username=val)
    val = request.GET['usergroup']
    user_list = models.User_New.objects.filter(user_group__caption=val) #对象就是一行数据，在模板里面获取数据的时候可以用对象.属性字段，但是在数据库中查询数据的时候就得用对象__属性字段（即双下划线）
    return render(request,'forign/create_user.html',{'obj':obj,'user_list':user_list})

