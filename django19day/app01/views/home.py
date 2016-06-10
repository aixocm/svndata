#!/usr/bin/env python
# -*- coding:utf-8 -*-
from    django.shortcuts import    render
from   app01.forms   import   home  as HomeForm
from app01  import  models
def  index(request):
    # models.UserInfo.objects.all().delete()
    # models.UserInfo.objects.create(name="JJJJJ")
    #
    # after = models.UserInfo.objects.all()
    # print after[0].ctime
    # dic = {'username':'alex','password':'123'}
    # models.SimpleModel.objects.create(**dic)
    ret = models.SimpleModel.objects.all()
    print ret,type(ret)
    ret = models.SimpleModel.objects.all().values('username')
    print ret,type(ret)
    ret = models.SimpleModel.objects.all().values_list('id','username')
    print ret,type(ret)
    obj = HomeForm.ImportForm()
    return render(request,'home/index.html',{'obj':obj})

def   upload(request):
    if request.method == "POST":
        inp_post = request.POST
        inp_files = request.FILES
        file_obj  =  inp_files.get('file_name')
        print file_obj.name
        print  file_obj.size
        f=open(file_obj.name,'wb')
        for line  in file_obj.chunks():
            f.write(line)
        f.close()
    return  render(request,'home/upload.html')
