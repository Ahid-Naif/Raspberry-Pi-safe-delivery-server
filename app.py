import serial, string
import time
import requests

ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
while True:
    readQR = ser.readline().decode('utf-8')
    
    print('readSerial:')
    print(readQR)
    if readQR == '':
        print('No readings')
    else:
        code = requests.get('https://hsbr-burger.com/checkBoxCode')
        print('response:')
        print(code.text)
        if readQR == code:
            print("True Code")
        else:
            print("Wrong Code")