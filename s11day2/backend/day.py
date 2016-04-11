#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import dayday
def month_fun(username):
    while True:
        Time=time.strftime('%Y-%m')
        with open(username,'ab') as f:
            f.write('[%s]\n'%Time)
        dayday.dayday_fun(username)