# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import  redirect,HttpResponse,render_to_response
# Create your views here.

def login(request):
    print request.method
    if request.method == 'POST':
        input_email = request.POST['email']
        input_pwd = request.POST['pwd']
        if input_email == 'JJ@qq.com' and input_pwd == "123":
            from django.shortcuts import   redirect
            # return redirect("https://www.baidu.com")
            return redirect("/index/")
        else:
            return  render(request,'login.html',{'status':'用户名或密码错误'})
    return render(request,'login.html')
def son(request):
    return render(request,'son1.html')

def  home(request):
    # return  HttpResponse('OK')
    dic = {'name':'LinJunJie','sex':1234567890,'user_list':['123','abc']}
    return render(request,'home.html',dic)

def  index(request):
    from app01 import models
    if request.method == "POST":
        input_em = request.POST['em']
        input_pw = request.POST['pw']
        #models.UserInfo.objects.create(email=input_em,pwd=input_pw)
        #models.UserInfo.objects.filter(email=input_em).delete()
        models.UserInfo.objects.filter(email=input_em).update(pwd=999999999)
    user_info_list = models.UserInfo.objects.all()
    return  render(request,'index.html',{'user_info_list':user_info_list})
