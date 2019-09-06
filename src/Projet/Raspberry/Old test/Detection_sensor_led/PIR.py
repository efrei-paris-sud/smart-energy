import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN) #PIR
#GPIO.setup(11, GPIO.OUT) #Led

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if not GPIO.input(17):
 #           GPIO.output(11, True)
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
  #          GPIO.output(11, False)
            print("Motion Detected...")
            time.sleep(4) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except KeyboardInterrupt:
    	print("Quitting")
