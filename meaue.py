#!/usr/bin/env  python
#-*- coding:utf-8 -*-
city_map = {"河北省":{"石家庄市":['平山县','无极县','灵寿县'],
                    "衡水市":['饶阳县','安平县','武强县']
                    },
            "山东省":{"济南市":['济阳县','商河县','平阴县'],
                    "青岛市":['市南区','市北区','市东区'],
                   },
            "河南省":{"洛阳市":['新安县','洛宁县','宜阳县'],
                    "郑州市":['金水区','惠济区','上街区']
                   }
}
for province in city_map.keys():
    print province
count =0
while count<3:
    shen = raw_input('please input your shen:')
    if shen in city_map.keys():
        while True:
            for shi in city_map[shen].keys():
                print shi,
            print   
            shi = raw_input('please input your shi:')
            if shi == 'quit':
                break
            elif shi in city_map[shen].keys():
                for xian in city_map[shen][shi]:
                    print xian,
            else:
                continue    
    else:
        if shen == 'quit':
            print "quited!"
            break
        continue
