import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
    i=GPIO.input(13)
    if i==False:                 #When output from motion sensor is LOW
        print "No intruders",i
        #GPIO.output(3, 0)  #Turn OFF LED
        time.sleep(0.5)
    else:              #When output from motion sensor is HIGH
        print "Intruder detected",i
        #GPIO.output(3, 1)  #Turn ON LED
        time.sleep(0.5)