#!/usr/bin/env python3
#coding:utf-8

import string
import random
import sys
from datetime import datetime,timedelta
from config import config;
import serial 
from font_1 import *

inv_date = '2018-08-20'
time_begin = '03:30'
# time_end = '16:35'
price = config.get('day_price',1.82)
# mile = 2.7
wait_time = '00:02:07'
cost = 36


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
    return '{}A,' + ''.join(car_no)


def get_comany():
    return random.sample(['10703','10724','10723','10745'],1)[0]    


def get_telephone():
    pre = ['22','23','24','25','26','27','28','88']
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


def printer_init():
    ser.write([ESC,64])             #ESC @   init the printer
    ser.write([ESC,99,0])           #ESC c 0 reverse the direction
    #defind liao
    for k in d:
        ser.write([ESC,ord('&'),ord(k)] + calc_hex(d[k]))
        ser.write([ESC,ord('%'),ord(k),ord(k),0]) 
    #设置行间距 6点
    ser.write([ESC,ord('1'),5])   

# wait_time = "00:%02d:%02d"%(random.uniform(0,2),random.uniform(0,59))
mile = get_mile(cost)
# cost = 9
time_end = get_end_time(time_begin,get_time(get_mile(cost)))

ESC=27
# ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser = serial.Serial('COM4', 9600, timeout=1)
printer_init()


ser.write(b"       " + car_no.encode("ascii") + b"\n")
ser.write(b"           " + company.encode("ascii") + b"\n")
ser.write(b"        " + telephone.encode("ascii") + b"\n")
ser.write(b"      " + inv_date.encode("ascii") + b"\n")
ser.write(b"           " + time_begin.encode("ascii") + b"\n")
ser.write(b"           " + time_end.encode("ascii") + b"\n")
ser.write([ESC,ord(':')])
printer_init()
ser.write(b"          " + ("%0.2f"%config.get('day_price',1.82)).encode("ascii") + b"\n")
ser.write(b"         " + ("%0.1f"%mile).encode("ascii") + b"\n")
ser.write(b"        " + wait_time.encode("ascii") + b"\n")
ser.write(b"          " + ("%0.2f"%cost).encode("ascii") + b"\n")
ser.write(b" \n")
# ser.write(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-;,.{}\n")
