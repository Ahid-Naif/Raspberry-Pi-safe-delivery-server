import serial, string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # GPIO Assign mode

GPIO.setup(3, GPIO.OUT)
pwm3=GPIO.PWM(3, 50)
GPIO.setup(5, GPIO.OUT)
pwm5=GPIO.PWM(5, 50)
pwm3.start(0)
pwm5.start(0)

ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
while True:
    readQR = ser.readline()
    
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
            _ = requests.get('https://hsbr-burger.com/remote_open_box')
            # GPIO.output(18, GPIO.HIGH) # lock on
            # time.sleep(1)
            # #
            # angle = 90
            # duty = angle / 18 + 2
            # GPIO.output(3, True)
            # GPIO.output(5, True)
            # pwm3.ChangeDutyCycle(duty)
            # pwm5.ChangeDutyCycle(duty)
            # time.sleep(1)
            # GPIO.output(3, False)
            # GPIO.output(5, False)
            # pwm3.ChangeDutyCycle(0)
            # pwm5.ChangeDutyCycle(0)
            # #
            # time.sleep(5)
        else:
            pass
        # else:
        #     print("Wrong Code")
        #     GPIO.output(18, GPIO.LOW) # lock off
        #     time.sleep(1)
        #     #
        #     angle = 0
        #     duty = angle / 18 + 2
        #     GPIO.output(3, True)
        #     GPIO.output(5, True)
        #     pwm3.ChangeDutyCycle(duty)
        #     pwm5.ChangeDutyCycle(duty)
        #     time.sleep(1)
        #     GPIO.output(3, False)
        #     GPIO.output(5, False)
        #     pwm3.ChangeDutyCycle(0)
        #     pwm5.ChangeDutyCycle(0)
        #     #
        time.sleep(1)