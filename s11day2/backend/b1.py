#!/usr/bin/env python
# -*- coding:utf-8 -*-
def fun():
    print 'blog,bbs,web'
    global s
    with open('C:\Users\Administrator\Desktop\haproxy.txt','r') as f:
        s=list(f)
    select = raw_input('please input fun :')
    value = raw_input('please input value:')
    global value_dict
    value_dict  = {'web':'backend server_web\n','blog':'backend server_blog\n','bbs':'backend server_bbs\n'}

    if select == 'q':
        query(value)
    if select == 'a':
        add(value)
    if select == 'd':
        delete(value)
    if select == 'c':
        change(value)

def  query(value):
    if value in value_dict.keys():
        if value_dict[value] in s:
            if value_dict[value] is not value_dict['bbs']:
                index = s.index(value_dict[value])
                for i in range(index+1,len(s)):
                    if s[i].startswith('###'):
                        break
                    print s[i],
            else:
                index = s.index(value_dict['bbs'])
                for i in s[index+1:]:
                    print i,
        else:
            print 'the dict is error'
    else:
        print 'input error'

def  add(value):
    if value in value_dict.keys():
        if value_dict[value] in s:
            if value_dict[value] is not value_dict['bbs']:
                index = s.index(value_dict[value])
                for i in range(index+1,len(s)):
                    if   s[i].startswith('###'):
                        ADD = raw_input('please insert your string:')
                        s.insert(i-1,ADD)
                        with open('C:\Users\Administrator\Desktop\haproxy.txt','w') as f:
                            f.writelines(s)
                        break
            else:
                ADD = raw_input('please insert your string:')
                s.append(ADD)
                with open('C:\Users\Administrator\Desktop\haproxy.txt','w') as f:
                    f.writelines(s)
        else:
                print 'the dict is error'
    else:
        print "input error"

def  delete(value):
    if value in value_dict.keys():
        if value_dict[value] in s:
            if value_dict[value] is not value_dict['bbs']:
                index = s.index(value_dict[value])
                for i in range(index+1,len(s)):
                    if   s[i].startswith('###'):
                        for num in range(len(s[index+1:i])):
                            print num,s[index+1+num]
                        break
                del_num = int(raw_input('please input your del_num:'))
                if del_num in  range(len(s[index+1:i])):
                    del s[index+1+del_num]
                    with open('C:\Users\Administrator\Desktop\haproxy.txt','w') as f:
                        f.writelines(s)
                else:
                    print "the del_num is error"
            else:
                index = s.index(value_dict['bbs'])
                for num in range(len(s[index+1:])):
                    print num,s[index+1+num]
                del_num = int(raw_input('please input your del_num:'))
                if del_num in  range(len(s[index+1:])):
                    del s[index+1+del_num]
                    with open('C:\Users\Administrator\Desktop\haproxy.txt','w') as f:
                        f.writelines(s)
                else:
                    print "the del_num is error"
        else:
            print 'the dict is error'
    else:
        print "input error"

def  change(value):
    if value in value_dict.keys():
        if value_dict[value] in s:
            if value_dict[value] is not value_dict['bbs']:
                index = s.index(value_dict[value])
                for i in range(index+1,len(s)):
                    if   s[i].startswith('###'):
                        for num in range(len(s[index+1:i])):
                            print num,s[index+1+num]
                        break
                change_num = int(raw_input('please input your change_num:'))
                if change_num in  range(len(s[index+1:i])):
                    changed_string = raw_input('please input your changed string:')
                    s[index+1+change_num]=changed_string+'\n'
                    with open('C:\Users\Administrator\Desktop\haproxy.txt','w') as f:
                        f.writelines(s)
                else:
                    print "the change_num is error"
            else:
                index = s.index(value_dict['bbs'])
                for num in range(len(s[index+1:])):
                    print num,s[index+1+num]
                change_num = int(raw_input('please input your change_num:'))
                if change_num in  range(len(s[index+1:])):
                    changed_string = raw_input('please input your changed string:')
                    s[index+1+change_num]=changed_string+'\n'
                    with open('C:\Users\Administrator\Desktop\haproxy.txt','w') as f:
                        f.writelines(s)
                else:
                    print "the change_num is error"
        else:
            print 'the dict is error'
    else:
        print "input error"

fun()