# import libraries that we need
import string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
# raspberry pi has two types of numbering
GPIO.setmode(GPIO.BOARD)   # we want to use physical pin numbering
# assign GPIO number 18 as OUTPUT as it's connected with the solenoid lock
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH) # also, set initial state as HIGH to keep the lock closed

# assign GPIO number 3 as OUTPUT as it's connected with the 1st servo motor
GPIO.setup(3, GPIO.OUT)
pwm3=GPIO.PWM(3, 50)
pwm3.start(0)

# assign GPIO number 3 as OUTPUT as it's connected with the 2nd servo motor
GPIO.setup(5, GPIO.OUT)
pwm5=GPIO.PWM(5, 50)
pwm5.start(0)

# while True means that all of the code below will run for ever to check box open/close
while True:
    time.sleep(5) # wait function.. check box status every 5 seconds

    # check status of the box from the server and stores the value at isBoxOpen variable
    isBoxOpen = requests.get('https://hsbr-burger.com/isBoxOpen')
    if isBoxOpen.text == '1': # if box is open
        GPIO.output(18, GPIO.LOW) # lock on
        # the two servos are open
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
    else: # else, if the box status is closed
        GPIO.output(18, GPIO.HIGH) # lock off
        # servos are closed
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
    