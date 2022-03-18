# 201801285 컴퓨터전자시스템공학부 김희찬

import serial
from escpos.constants import GS

print("응 이미 바꿨어")

def openSer(port, baudrate = 9600, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, timeout = None, xonxoff = False, rtscts = False, dsrdtr = False):
    ser = serial.Serial()

    ser.port = port
    ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity = parity
    ser.stopbits = stopbits
    ser.timeout = timeout
    ser.xonxoff = xonxoff
    ser.rtscts = rtscts
    ser.dsrdtr = dsrdtr

    ser.open()
    return ser

ser = openSer('COM5')

#a = chr(0x0A)

for _ in range(1):
    pass
    #ser.write(a.encode())  # UTF-8



print('aaaaaaaaaa')

#a = b'\x0A'   # a = '0x0A', a = a.encode()
#ser.write(a)

b = b'\x1D\x56\67\255'
c = GS + b"V" + six.int2byte(66) + b"\x00"
ser.write(b)

ser.close()
