# import libraries that we need
import serial, string
import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
# raspberry pi has two types of numbering
GPIO.setmode(GPIO.BOARD) # we want to use physical pin numbering
# assign GPIO number 18 as OUTPUT as it's connected with the solenoid lock
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # also, set initial state as HIGH to keep the lock closed

# assign GPIO number 3 as OUTPUT as it's connected with the 1st servo motor
GPIO.setup(3, GPIO.OUT)
pwm3=GPIO.PWM(3, 50)
pwm3.start(0)

# assign GPIO number 3 as OUTPUT as it's connected with the 2nd servo motor
GPIO.setup(5, GPIO.OUT)
pwm5=GPIO.PWM(5, 50)
pwm5.start(0)

# define seria port to be able to read QR codes
ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)

# while True means that all of the code below will run 
# as long as the raspberry is on to read QR codes
while True:
    # read QR code and stores the value in readQR variable
    readQR = ser.readline()
    
    
    if readQR == str.encode(''): # if there is no readings
        pass # ignore it
    else: # else, if there is a reading
        # check the correct code from the server
        code = requests.get('https://hsbr-burger.com/checkBoxCode')
        if readQR[0:6] == str.encode(code.text): #if they match

            # send a request to change the status of the box into open
            _ = requests.get('https://hsbr-burger.com/remote_open_box')
           
        else: # else, if the read qr code is wrong
            pass # ignore it
       
        # wait for 1 second to give some time to the raspbeery to communicate with the server
        time.sleep(1)