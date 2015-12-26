#!/usr/bin/env python
# coding:utf-8
with open('C:\Users\Administrator\Desktop\user.txt','r') as f:
	user_info = f.readlines()
user_dict={}
for line in user_info:
	name = line.split(':')	
	user_dict[name[0]] =[str(name[1]),int(name[2].strip())]	
def fun_user():
    new_user_info = []
    for user_key in user_dict.keys():
        user_info = "%s:%s:%d" % (user_key,user_dict[user_key][0],user_dict[user_key][1])
        new_user_info.append(user_info)
        newuserinfo='\n'.join(new_user_info)
        with open('C:\Users\Administrator\Desktop\user.txt','w') as f:
            f.write(newuserinfo)
            f.flush()
count=0
while True:
    name=raw_input('please input your name:')
    passwd=raw_input('please input your passwd:')
    if name  not in user_dict.keys():
        count+=1
        if count >=3:
            print "please ask adminstrator for help"
            break
        else:
            continue
    if name in user_dict.keys():
        if user_dict[name][1] <2:
            if passwd == user_dict[name][0]:
                print "Thanks login the system!"
                user_dict[name][1]=0
                fun_user()
                break
            else:
                user_dict[name][1]+=1
                fun_user()
                print "your passwd is error"
                continue
        else:
            if user_dict[name][1] == 2 and passwd == user_dict[name][0]:
                user_dict[name][1]=0
                fun_user()
                print "Thanks login the system!"
                break
            print "your passwd is error,please ask adminstrator for help "
            user_dict[name][1]+=1
            fun_user()
            break
