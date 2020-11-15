import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
GPIO.setup(5, GPIO.OUT)
pwm=GPIO.PWM(5, 50)
pwm.start(0)

while True:
    #
    angle = 0
    duty = angle / 18 + 2
    GPIO.output(3, True)
    GPIO.output(5, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(3, False)
    GPIO.output(5, False)
    pwm.ChangeDutyCycle(0)
    #
    time.sleep(3)
    #
    angle = 90
    duty = angle / 18 + 2
    GPIO.output(3, True)
    GPIO.output(5, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(3, False)
    GPIO.output(5, False)
    pwm.ChangeDutyCycle(0)
    #