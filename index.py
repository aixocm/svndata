#!/usr/bin/env python
# -*- coding:utf-8 -*-
store={1:{'牛奶':'10元'},2:{'巧克力':'5元'},3:{'苹果':'7元'},4:{'口香糖':'3元'},5:{'矿泉水':'2元'},6:{'菠萝':'6元'},7:{'饼干':'4元'}}
with open('C:\Users\Administrator\Desktop\info.txt','r')  as f:
    k=f.readlines()
user_dict = {}
for i in k:
    user_name=i.split(':')[0]
    user_passwd=str(i.split(':')[1])
    user_money=int(i.split(':')[2].strip())
    user_dict[user_name]={user_passwd:user_money}
for i in user_dict.keys():
    print i,user_dict[i].keys()[0],user_dict[i].values()[0]
flag=1
while flag:
    global name
    name = raw_input('请输入你的用户名:')
    if name == 'Q':
        break
    passwd=raw_input('请输入你的密码:')
    if passwd == 'Q':
        break
    if name in user_dict.keys() and passwd == str(user_dict[name].keys()[0]):
        print "欢迎登录购物车小程序！"
        for  id  in store:
            print id,
            for i in store[id]:
                print i,store[id][i]
        buyed={}
        seq=[]
        user_money_sum=user_dict[name].values()[0]
        for n in range(1,8):
            seq.append(store[n].keys()[0])
        buyed=buyed.fromkeys(seq,0)

        while True:
            print "退出购物车小程序请输入88"
            num_id=int(raw_input("请输入你想购买的商品编号:"))
            if num_id == 88:
                flag=0
                break
            num_num=int(raw_input("请输入你购买此商品的数量:"))
            if num_num == 88:
                flag=0
                break
            print user_dict[name].values()[0]
            print int(store[num_id].values()[0][:-3])*num_num
            if user_dict[name].values()[0]  < int(store[num_id].values()[0][:-3])*num_num:
                print "对不起，您的余额不足，不能购买"
            else:
                print "添加到购物车成功！"
                buyed[store[num_id].keys()[0]]+=num_num
                user_money_sum-=int(store[num_id].values()[0][:-3])*num_num
                user_dict[name]={user_dict[name].keys()[0]:user_money_sum}

            result = raw_input('是否结算,结算请输入y,不结算请输入n:')
            if result == 'y':
                userinfo=[]
                for info in user_dict.keys():
                    user_info="%s:%s:%d" %(info,user_dict[info].keys()[0],user_dict[info].values()[0])
                    userinfo.append(user_info)
                    new_user_info='\n'.join(userinfo)
                    with open('C:\Users\Administrator\Desktop\info.txt','w')  as f:
                        f.write(new_user_info)
                        f.flush()
                print "此次你购买的商品名单和数量为:"
                for thing in  buyed.keys():
                    print thing,buyed[thing]
                flag=0
                break
            if result == 'n':
                continue
    else:
        print "用户名或密码错误，请重新输入,输入 Q 结束！"
        continue

