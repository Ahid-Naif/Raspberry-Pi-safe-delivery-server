import serial, string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
lock = 23
GPIO.setup(lock, GPIO.OUT) # GPIO Assign mode

ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
while True:
    readQR = ser.readline()
    
    print('readSerial:')
    print(readQR)
    if readQR == '':
        print('No readings')
        GPIO.output(lock, GPIO.LOW) # lock off
    else:
        code = requests.get('https://hsbr-burger.com/checkBoxCode')
        print('response:')
        print(code.text)
        if unicode(readQR) == unicode(code.text):
            print("True Code")
            GPIO.output(lock, GPIO.HIGH) # lock off
        else:
            print("Wrong Code")
            GPIO.output(lock, GPIO.LOW) # lock off
        time.sleep(1)