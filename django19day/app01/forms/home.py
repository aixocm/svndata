#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  django   import   forms
from  app01   import  models
class  ImportForm(forms.Form):
    HOST_TYPE_LIST = (
        (1,'物理机'),
        (2,'虚拟机')
    )
    host_type = forms.IntegerField(
        widget=forms.Select(choices=HOST_TYPE_LIST)
    )
    hostname = forms.CharField()
    import json
    # dic  = ((1,'sdsad'),(2,'sadasdadsfdsfs'))
    # f = open('db_admin','w')
    # f.write(json.dumps(dic))
    # f.close()
    fr=open('db_admin')
    data = fr.read()
    data_tuple = json.loads(data)
    fr.close()
   # password = forms.CharField(widget=forms.PasswordInput())
    admin =  forms.IntegerField(
        widget=forms.Select(choices=data_tuple)
    )
    def  __init__(self,*args,**kwargs):
        super(ImportForm, self).__init__(*args,**kwargs)
        # import json
        # fr=open('db_admin')
        # data = fr.read()
        # data_tuple = json.loads(data)
        # self.fields['admin'].widget.choices = data_tuple
        self.fields['admin'].widget.choices = models.SimpleModel.objects.all().values_list('id','username')