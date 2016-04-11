#!/usr/bin/env python
# -*- coding:utf-8 -*-
#date:2016-1-11
import time
import hashlib
import pickle
import ConfigParser
import day
info = {}
def regiest():
    global info
    while True:
        username = raw_input('please input your username:')
        passwd = raw_input('please input your password:')
        if not (username and passwd):
            print 'your username or password is empty'
            continue
        else:
            with open('user.txt','a+') as f:
                string = f.read()
            if string == "":
                hash = hashlib.md5('JJ')
                hash.update(passwd)
                ret = hash.hexdigest()
                info[username]=[ret,15000]
                f = open('user.txt','wb')
                pickle.dump(info,f)
                f.close()
                print 'regiest is sucessful!'
                day.month_fun(username)
                # dayday.dayday_fun(username)
            else:
                f=open('user.txt','rb')
                info = pickle.load(f)
                f.close()
                if username in info.keys():
                    print 'This  user is already exist!'
                    continue
                else:
                    hash = hashlib.md5('JJ')
                    hash.update(passwd)
                    ret = hash.hexdigest()
                    info[username]=[ret,15000]
                    f = open('user.txt','ab')
                    pickle.dump(info,f)
                    f.close()
                    print 'regiest is sucessful!'
                    day.month_fun(username)
                    # dayday.dayday_fun(username)
def login():
    global info
    global username
    f=open('user.txt','rb')
    info = pickle.load(f)
    f.close()
    username = raw_input('please input your name:')
    passwd = raw_input('please input your password:')
    if username not in info.keys():
        print  'please  regiest!'
        regiest()
    else:
        hash = hashlib.md5('JJ')
        hash.update(passwd)
        ret = hash.hexdigest()
        if username in info.keys() and ret in info[username][0]:
            print 'login successful!'
            return True
        else:
            print 'login is failure'
            return False

def get_money(username):
    global info
    if info[username][1] < 0:
        print 'sorry,please the money'
    else:
        num = int(raw_input('please input your money num:'))
        if info[username][1] - num*1.05 >= 0:
            info[username][1] -= num*1.05
            f = open('user.txt','wb')
            pickle.dump(info,f)
            f.close()
            print 'get money is sucessful!'
        else:
            print 'sorry,you get money is too much'

def return_money(username):
    global info
    value_add=int(raw_input('please input your money:'))
    with open('add.txt','a+') as f:
        value=int(f.read())
    with open('add.txt','wb') as f:
        f.write(value+value_add)
    info[username][1]=15000+value_add+value-Sum
    f = open('user.txt','wb')
    pickle.dump(info,f)
    f.close()
    print '已充值!'
def account_list(username):
    global info
    global Sum
    with open('add.txt','a+') as f:
        value=f.read()
    if value == "":
        value=0
        with open('add.txt','wb') as f:
            f.write(value)
    config = ConfigParser.ConfigParser()
    config.read(username)
    month_list=config.sections()
    Sum=0
    for month in  month_list:
        key_list=config.items(month)
        print month,"的账单如下:"
        for  opt  in  key_list:
            print opt[0],":",opt[1]
            Sum+=config.getint(month,opt[0])

    if  15000 - Sum + int(value) < 0:
        print  '你已经欠款',15000 - Sum + int(value)
        k=raw_input('if you add your money,please input A')
        if k == 'A':
            return_money(username)
        else:
            print 'your input is error'

    else:
        info[username][1]-=Sum
        f = open('user.txt','wb')
        pickle.dump(info,f)
        f.close()

def M
    flag = raw_input("if you regiest,please input 'R',if you login,please input 'L':")
    if flag == 'R':
        regiest()
    elif flag == 'L':
        if login():
            select = raw_input("get money input G,query your account_list input Q:")
            if  select == 'G':
                get_money(username)
            if  select =='Q':
                if int(time.time()) > 0:
                    account_list(username)
                else:
                    print 'date is do not to'
    else:
        print 'your input is error'
Main()



