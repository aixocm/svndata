#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
str1 = raw_input('please input str:')
str2=str(str1)

def replaced(str2):
    if str2.__contains__('--') or str2.__contains__('-+') or str2.__contains__('+-'):
        str2=re.sub('\-\-','+',str2)
        str2=re.sub('\-\+','-',str2)
        str2=re.sub('\+\-','-',str2)
        str2=re.sub('\s*','',str2)
    return str2

def add_reduce(str1,str2,rep):
    if re.search('\-?\d+\.*\d*\+\-?\d+\.*\d*',rep):
        str1=re.search('\-?\d+\.*\d*\+\-?\d+\.*\d*',rep).group()
        rep=str1
        str1 = str(float(str1.split('+')[0])+float(str1.split('+')[1]))

    if re.search('\-?\d+\.*\d*\-\-?\d+\.*\d*',rep):
        str1=re.search('\-?\d+\.*\d*\-\-?\d+\.*\d*',rep).group()
        rep=str1
        str1 = str(float(str1.split('-')[0])-float(str1.split('-')[1]))

    str2=str2.replace(rep,str1)
    return str2

def  multi_divmod(str1,str2,rep):
    if re.search('\-?\d+\.*\d*\*\-?\d+\.*\d*',rep):
        str1=re.search('\-?\d+\.*\d*\*\-?\d+\.*\d*',rep).group()
        rep=str1
        str1 = str(float(str1.split('*')[0])*float(str1.split('*')[1]))

    if re.search('\-?\d+\.*\d*\/\-?\d+\.*\d*',rep):
        str1=re.search('\-?\d+\.*\d*\/\-?\d+\.*\d*',rep).group()
        rep=str1
        str1 = str(float(str1.split('/')[0])/float(str1.split('/')[1]))

    str2=str2.replace(rep,str1)
    return str2

def excute(str1,str2,rep):
    if str1.__contains__('*') or str1.__contains__('/'):
        str2=multi_divmod(str1,str2,rep)

    if str1.__contains__('+') or str1.__contains__('-'):
        str2=add_reduce(str1,str2,rep)

    str2=replaced(str2)
    return str2

def regex(str1,str2):
    if  re.search('\([^()]*\)',str2):
        rep = str(re.search('\([^()]*\)',str2).group())
        str1=rep[1:-1]
        if re.search('\-?\d+\.*\d*[\+\-\/\*]\-?\d+\.*\d*',str1):
            str2 = excute(str1,str2,rep)
        elif  re.search('\-?\d+\.*\d*',str1):
            str2=str2.replace(rep,str1)
            str2=replaced(str2)
        else:
            print 'no string have get it'
    else:
        if  re.search("\-?\d+\.*\d*[\+\-\*\/]\-?\d+\.*\d*",str2):
            rep=re.search("\-?\d+\.*\d*[\+\-\*\/]\-?\d+\.*\d*",str2).group()
            str1 = rep
            str2=excute(str1,str2,rep)
        else:
            if re.search('\-?\d+\.*\d*',str2):
                print str2
                return
            else:
                print 'input is error'
                return
    return regex(str1,str2)

regex(str1,str2)