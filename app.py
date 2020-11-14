import serial, string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
lock = 16
GPIO.setup(lock, GPIO.OUT, initial=GPIO.LOW) # GPIO Assign mode

ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
while True:
    GPIO.output(lock, GPIO.LOW) # lock off
    time.sleep(3)
    GPIO.output(lock, GPIO.HIGH) # lock on
    time.sleep(3)
# while True:
#     readQR = ser.readline()
    
#     print('readSerial:')
#     print(readQR)
#     if readQR == str.encode(''):
#         print('No readings')
#         GPIO.output(lock, GPIO.LOW) # lock off
#     else:
#         code = requests.get('https://hsbr-burger.com/checkBoxCode')
#         print('response:')
#         print(code.text)
#         if readQR[0:6] == str.encode(code.text):
#             print("True Code")
#             GPIO.output(lock, GPIO.HIGH) # lock on
#         else:
#             print("Wrong Code")
#             GPIO.output(lock, GPIO.LOW) # lock off
#         time.sleep(1)