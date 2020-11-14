import serial, string
import time
import requests

output = " "
ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
while True:
        readQR = ser.readline().decode('utf-8')
        code = requests.get('https://hsbr-burger.com/checkBoxCode')
        print(code.text)
        if readQR == code:
                print("True Code")
                time.sleep(1)
        else:
                print("Wrong Code")