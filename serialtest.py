#!/usr/bin/env python3
#coding=utf-8
#测试serial

import serial  

ESC=27
SP=32
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

INIT=[27,64]

ser.write(INIT)
ser.write([27,ord('c'),0])
ser.write(b"AAA\n")
