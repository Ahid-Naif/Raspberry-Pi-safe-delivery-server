import string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # GPIO Assign mode

while True:
    time.sleep(5)
    isBoxOpen = requests.get('https://hsbr-burger.com/isBoxOpen')
    if isBoxOpen.text == '1':
        GPIO.output(18, GPIO.HIGH) # lock on
        time.sleep(5)
    else:
        GPIO.output(18, GPIO.LOW) # lock off
    