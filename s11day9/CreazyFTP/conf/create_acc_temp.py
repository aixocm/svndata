#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

acc_dic = {
    'alex':{
        "password":"123",
        "quotation":1000000,
        "expire_date":"2016-01-02"

    },
    'dali':{ "password":"234",
        "quotation":1000000,
        "expire_date":"2016-01-03"},
    'dalimei':{},
    'dalimei2':{},

}
f=file("accounts.json",'wb')
json.dump(acc_dic,f)
f.close()