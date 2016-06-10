#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import   render,render_to_response,HttpResponse
from  app01.forms  import   account  as   AccountForm
def login(request):
    obj = AccountForm.LoginForm(request.POST)
    if  request.method == "POST":
        if obj.is_valid():
            all_data = obj.clean()
        else:
            #form表单提交
            # error = obj.errors
            # print type(error)
            # print error['username'][0]
            # print error['password'][0]
            #Ajax
            error = obj.errors.as_json()
            return HttpResponse(error)
            print error,type(error)
        return render(request,'account/login.html',{ 'obj':obj,'error':error })
    return render(request,'account/login.html',{'obj':obj})
