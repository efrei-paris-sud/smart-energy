import time
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
import os
import glob


#Config:
GPIO.setmode(GPIO.BCM)
GPIO_PIR = 37
sensor_args = { '11': Adafruit_DHT.DHT11,

                '22': Adafruit_DHT.DHT22,

                '2302': Adafruit_DHT.AM2302 }

os.system('modprobe wl-gpio')
os.system('modprobe wl-therm')
base_dir = '/sys/bus/w1/devices/'

device_folder = glob.glob(base_dir + '28*')[0]

device_file = device_folder + '/w1_slave'

GPIO.setup(GPIO_PIR,GPIO.IN)


#Setting time:
TIME_START = time.time()
current_time = TIME_START
WAITING_TIME = 30 #Temps en secondes entre chaque mesure


#Setting save:
fichier = open("save.txt", "w")


#Initialization:
Current_PIR_State = 0
Previous_PIR_State = 0
try:
	print ("Waiting for PIR to settle...")
	while (GPIO.input(GPIO_PIR) == 1):
		Current_PIR_State = 0
	print ("PIR ready")


#Running:

	while (True):
		current_time = time.time() - TIME_START
		#print(str(int(current_time)))
		#print('\n')

		dataPIR, Current_PIR_State, Previous_PIR_State = PIR_run(Current_PIR_State, Previous_PIR_State)
		dataTempHumi = TempHumi_run()
		dataSonde = Sonde_run()

		data_all = str(int(current_time)) + ' seconds : Inside' + dataTempHumi + '  ' + dataSonde + '  ' + dataPIR + '\n'
		#print('DATA_ALL = ' + data_all)
		fichier.write(data_all)

		time.sleep(WAITING_TIME)


#Si on ferme le programme (CTRL+C):
except KeyboardInterrupt:
	print ("Quitting...")
	fichier.close()
	GPIO.cleanup()










def PIR_run(Current_PIR_State, Previous_PIR_State):
        Current_PIR_State = GPIO.input(GPIO_PIR)

    if Current_PIR_State==1 and Previous_PIR_State==0:

		#print "Motion detected"
        	dataPIR = "Motion detected"
        	Previous_State=1

    elif Current_PIR_State==0 and Previous_PIR_State==1:

            	#print "No new motion detected, PIR Ready"
	dataPIR = "No new motion detected"
       	Previous_PIR_State=0


    return dataPIR, Current_PIR_State, Previous_PIR_State


def TempHumi_run():
	#Verif param :
	if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
		sensor = sensor_args[sys.argv[1]]
		pin = sys.argv[2]
	else:
		print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
		print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
		sys.exit(1)

	#Lecture donnees :
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		dataTempHumi = 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
		#print(dataTempHumi)
	else:
		print('TempHumi: Failed to ger reading. Try again!')
		sys.exit(1)

	return dataTempHumi


def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines


def Sonde_run():
	dataSonde = '  '
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		dataSonde = 'Temp ext: ' + str(temp_c) + '*C = ' + str(temp_f) + 'F'
		#print(dataSonde)
	return dataSonde

	


