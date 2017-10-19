#!/usr/bin/env python3
#coding=utf-8
#测试serial

import serial  

ESC=27
SP=32
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

INIT=[27,64]        #ESC @
REVERSE=[27,99,0]   #ESC c 0

ser.write(INIT)
ser.write(REVERSE)

#defind liao
ser.write([ESC,ord('&'),ord('{'),0x00,0x21,0xa1,0xa2,0x7e,0x02 ])
ser.write([ESC,ord('&'),ord('}'),0x81,0x85,0xbf,0xc1,0x81,0x00 ])
ser.write([27,0x25,ord('{'),ord('{'),ord('}'),ord('}'),0])
ser.write(b"{}A.1234J\n")
#reset 
ser.write([27,58])
