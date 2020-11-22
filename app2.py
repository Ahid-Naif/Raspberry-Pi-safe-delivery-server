import string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH) # GPIO Assign mode

GPIO.setup(3, GPIO.OUT)
pwm3=GPIO.PWM(3, 50)
GPIO.setup(5, GPIO.OUT)
pwm5=GPIO.PWM(5, 50)
pwm3.start(0)
pwm5.start(0)

while True:
    time.sleep(5)
    isBoxOpen = requests.get('https://hsbr-burger.com/isBoxOpen')
    if isBoxOpen.text == '1':
        GPIO.output(18, GPIO.LOW) # lock on
        #
        angle = 90
        duty = angle / 18 + 2
        GPIO.output(3, True)
        GPIO.output(5, True)
        pwm3.ChangeDutyCycle(duty)
        pwm5.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(3, False)
        GPIO.output(5, False)
        pwm3.ChangeDutyCycle(0)
        pwm5.ChangeDutyCycle(0)
        #
        time.sleep(5)
    else:
        GPIO.output(18, GPIO.HIGH) # lock off
        #
        angle = 0
        duty = angle / 18 + 2
        GPIO.output(3, True)
        GPIO.output(5, True)
        pwm3.ChangeDutyCycle(duty)
        pwm5.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(3, False)
        GPIO.output(5, False)
        pwm3.ChangeDutyCycle(0)
        pwm5.ChangeDutyCycle(0)
        #
    