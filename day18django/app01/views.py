#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render
# Create your views here.
from django.shortcuts import   render,HttpResponse
import time
from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.cache import cache_page
db = {'JJ':123456,'eric':11111111111111111111}
def  login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == "JJ" and pwd == "123":
            request.session['IS_LOGIN'] = True
            request.session['USERNAME'] = 'JJ'
            return redirect('/app01/home/')
        elif  username == "eric" and  pwd ==  "123":
            request.session['IS_LOGIN'] = True
            request.session['USERNAME'] = 'eric'
            return redirect('/app01/home/')
    return render(request,'login.html')
def home(request):
    is_login = request.session.get('IS_LOGIN',False)
    if is_login:
        username = request.session.get('USERNAME',False)
        data = db[username]
        #return HttpResponse(data)
        return render(request,'home.html',{'username':username})
    else:
        return redirect('/app01/login/')

def logout(request):
    del request.session['IS_LOGIN']
    return redirect('/app01/login/')
@cache_page(60 * 15)
def cache_page(request):
    current = str(time.time())
    return HttpResponse(current)

def  index(request):
    raise Exception('bbbbbbbbbbbbbb')
    return HttpResponse('ok')

def user_list(request,v1,v2):
    return HttpResponse(v1+v2)
