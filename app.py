import serial, string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # GPIO Assign mode

ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
while True:
    try:
        readQR = ser.readline()
    except Exception:
        print('Exception ERROR 1')
    else:
        print('readSerial:')
        print(readQR)
        if readQR == str.encode(''):
            print('No readings')
        else:
            code = requests.get('https://hsbr-burger.com/checkBoxCode')
            print('response:')
            print(code.text)
            if readQR[0:6] == str.encode(code.text):
                print("True Code")
                GPIO.output(18, GPIO.HIGH) # lock on
                time.sleep(5)
            else:
                print("Wrong Code")
                GPIO.output(18, GPIO.LOW) # lock off
            time.sleep(1)