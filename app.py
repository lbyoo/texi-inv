#!/usr/bin/env python3
#coding:utf-8

import string
import random
import sys
from datetime import datetime,timedelta
from config import config;



inv_date = '2017-10-07'
time_begin = '16:30'
time_end = '16:35'
price = config.get('day_price',1.82)
mile = 2.7
wait_time = '00:00:00'
cost = 9


'''
0-3 公里 8元，之后每公里1.82,等时每3分钟一元
'''

def get_car_no():

    alpha = string.ascii_uppercase.replace('I','').replace('O','')
    number = [str(x) for x in range(0,10)]
    n = random.randint(0,2)
    m = 5 - n
    car_no = random.sample(alpha,n)+random.sample(number,m)
    random.shuffle(car_no)
    # print(car_no)
    return '辽A.' + ''.join(car_no)


def get_comany():
    return random.sample(['0103','0102','0101'],1)[0]    


def get_telephone():
    pre = ['22','23','24','25','26','27','28']
    return random.sample(pre,1)[0] + ''.join([str(random.randint(0,9)) for x in range(0,6)])


car_no = get_car_no()
company = get_comany()
telephone = get_telephone()

def get_mile(cost):

    initial_price = config.get('initial_price',8)
    day_price = config.get('day_price',1.82)
    #如果费用小于起步价，提示错误
    if cost < initial_price:
        print("cost must greater %d" % initial_price)
        sys.exit(1)


    if cost ==     initial_price:
        mile = round(random.uniform(0,3),1)

    if cost > initial_price:
        tail = random.uniform(0,1/day_price)
        if cost - initial_price > 1:
            mile = round(3 + tail + (cost - initial_price - 1)/day_price,1)
        else:
            mile = round(3 + tail,1)

    return mile
    
def get_time(mile):
    s = mile/config.get("speed") * 3600
    return int(s)


def get_end_time(begin_time,seconds):
    ctime = datetime.strptime(begin_time,'%H:%M')
    return (ctime + timedelta(seconds = seconds)).strftime("%H:%M")

wait_time = "00:%02d:%02d"%(random.uniform(0,2),random.uniform(0,59))

mile = get_mile(cost)
cost = 8
print('%d:'%cost,get_mile(cost),get_time(get_mile(cost)))  
cost = 9
print('%d:'%cost,get_mile(cost),get_time(get_mile(cost)))    
# cost = 10
# print('%d:'%cost,get_mile(cost),get_time(get_mile(cost)))     
# cost = 500
# print('%d:'%cost,get_mile(cost),get_time(get_mile(cost)))   
time_end = get_end_time(time_begin,get_time(get_mile(cost)))
print('''%11s
%10s
%10s
%10s
%10s
%10s
%10s
%10s
%10s
%10.2f
'''%(car_no,company,telephone,inv_date,time_begin,time_end,config.get('day_price',1.82),
    mile,wait_time,cost))