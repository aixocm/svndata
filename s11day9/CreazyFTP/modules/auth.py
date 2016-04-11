#!/usr/bin/env python
# -*- coding:utf-8 -*-
from conf import settings
import json
import sys
def  fetch_account():
    acc_storage = settings.ACCOUNT_DB.get("engine")
    if hasattr(sys.modules[__name__],"engine_"+acc_storage):
        obj=getattr(sys.modules[__name__],"engine_"+acc_storage)
        return obj()
def authentication(user,passwd):
    engine_obj=fetch_account()
    return engine_obj.auth(user,passwd)

class  engine_file():
    def __init__(self):
        print 'engine file......'
    def auth(self,user,passwd):
        print "--------engine file......"
        filename=settings.ACCOUNT_DB.get("name")
        assert filename is not None
        f = file(filename,'rb')
        acc_dic = json.load(f)
        user_in_db=acc_dic.get(user)
        if user_in_db:
            if passwd == user_in_db.get("password"):
                msg='authentication succecssful'
                status = True
            else:
                msg = "username or password wrong"
                status =  False
        else:
            msg = "no such user"
            status =  False
        return  status,msg
class  engine_mysql():
    def auth(self,user,passwd):
        print "--------engine file......"
