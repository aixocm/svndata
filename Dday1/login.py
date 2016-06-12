#!/usr/bin/env python 
# coding:utf-8
i=0
while i < 3:
	name = raw_input('please input your name:')
	pwd = raw_input('please input your password:')
	if name == 'JJ' and pwd == '123':
		print 'success login!'
		break	
	i+=1
else:
		print 'you can not login again'
		
 
