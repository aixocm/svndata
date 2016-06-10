#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  django   import   forms
from  app01   import  models
class  UserForm(forms.Form):
    username = forms.CharField()
    # user_group =  forms.IntegerField(
    #     widget=forms.Select()   第一，二 种方法
    user_group_id =  forms.IntegerField(
         widget=forms.Select()
    )
    def  __init__(self,*args,**kwargs):
        super(UserForm, self).__init__(*args,**kwargs)

        self.fields['user_group_id'].widget.choices = models.UserGroup_New.objects.all().values_list('id','caption')