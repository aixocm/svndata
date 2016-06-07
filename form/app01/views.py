#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render
from  django import  forms
# Create your views here.
class UserInfo(forms.Form):
    user_type_choice = (
        (0,u'普通用户'),
        (1,u'高级用户'),
    )
    user_type = forms.IntegerField(error_messages={'required':u'用户类型不能为空'},
                                   widget=forms.widgets.Select(choices=user_type_choice,
    attrs={'class':"form-control"}))
    email = forms.EmailField(error_messages={'required':u'邮箱不能为空'})
    host = forms.CharField(error_messages={'required':u'主机不能为空'})
    port = forms.CharField(error_messages={'required':u'端口不能为空'})
    mobile = forms.CharField(error_messages={'required':u'手机不能为空'},
                             widget=forms.TextInput(attrs={'class':"form-control",'placeholder':u'手机号码'}))
    memo = forms.CharField(required=False,
                           widget=forms.Textarea(attrs={'class':"form-control",'placeholder':u'备注'}))
def  user_list(request):
    obj = UserInfo()
    # host = request.POST.get('host')
    # port = request.POST.get('port')
    # email = request.POST.get('email')
    # mobile = request.POST.get('mobile')
    if request.method == 'POST':
        user_input_obj = UserInfo(request.POST)
        if  user_input_obj.is_valid():
            data = user_input_obj.clean()
            print data
        else:
            error_msg = user_input_obj.errors
            return render(request,'user_list.html',{'obj':user_input_obj,'errors':error_msg})
    return render(request,'user_list.html',{'obj':obj})

from django.shortcuts import  HttpResponse
def ajax_data(request):
    print request.POST
    return HttpResponse("ok")

import  json
def  ajax_data_set(request):
    ret = {'status':True,'error':""}
    try:
        print request.POS
    except Exception,e:
        ret['status'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret))