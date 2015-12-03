#!/usr/bin/env python
# coding:utf-8
print  '''
	1 河南
	2 河北
	3 湖南
	'''
Province={'1':'河北','2':'河南','3':'湖南'}
HeB_list={'H':['撒大师','asdas','啊色达'],'HH':['dasd','tryr','sdfjhh'],'HHH':['duyt','uyl','ninincivbd']}
HeB_list_num={'1':'H','2':'HH','3':'HHH'}
HeN_list={'N':['mkmvkmvb','ninibnfg','jjojgg'],'NN':['nkjndgd','ndngiodjfgod','fghftujtjty'],'NNN':['ifhigd','fghdgddg','jonomo']}
HeN_list_num={'1':'N','2':'NN','3':'NNN'}
HuN_list={'U':['ashy5','nonnicb','mknjbjcxc'],'UU':['ut','jjovjx','njhnkhada'],'UUU':['mjijsidfsd','modjgodjgod','pkpkty']}
HuN_list_num={'1':'U','2':'UU','3':'UUU'}
while True:
    num = raw_input("please select your number,enter 'q' to quit:")
    if num == 'q':
        break
    if num == ''  or  num not in ('1','2','3'):
        continue
    if num == '1':
        print Province[num],':'
        print HeB_list.keys()
        key = raw_input('please input number:')
        print HeB_list[HeB_list_num[key]]
		
    if num == '2':
        print Province[num],':'
        print HeN_list.keys()
        key = raw_input('please input number:')
        print HeN_list[HeN_list_num[key]]
		
    if num == '3':
        print Province[num],':'
        print HuN_list.keys()
        key = raw_input('please input number:')
        print HuN_list[HuN_list_num[key]]
		
