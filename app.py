import serial, string
import time
import requests

ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
while True:
    readQR = ser.readline()
    
    print('readSerial:')
    print(readQR[0:6])
    if readQR == str.encode(''):
        print('No readings')
    else:
        code = requests.get('https://hsbr-burger.com/checkBoxCode')
        print('response:')
        print(code.text)
        if readQR[0:6] == str.encode(code.text):
            print("True Code")
        else:
            print("Wrong Code")
        time.sleep(1)