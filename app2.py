import string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH) # GPIO Assign mode

while True:
    isBoxOpen = requests.get('https://hsbr-burger.com/isBoxOpen')
    if isBoxOpen.text == '1':
        GPIO.output(18, GPIO.HIGH) # lock on
        time.sleep(5)
    else:
        GPIO.output(18, GPIO.LOW) # lock off
    time.sleep(3)