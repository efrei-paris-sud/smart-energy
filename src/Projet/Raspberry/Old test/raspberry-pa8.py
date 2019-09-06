import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import smbus


gpio_motionSensor = 11;
gpio_DHT = 27
type_DHT = 11 							#could be 22 if we upgrade
gpio_lightBarrier = 56
gpio_SDA = 2
gpio_SCL = 3

def lightBarrier():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_motionSensor, GPIO.IN)
    i = GPIO.input(gpio_motionSensor)

    if(i == 0):					#barrier crossed
        return False;
    elif(i == 1):				#barrier not crossed
        return True;

def getHumidityTemperature():
    humidity, temperature = Adafruit_DHT.read_retry(type_DHT, gpio_DHT)
    return humidity, temperature;

def motionSensorPIR():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_motionSensor, GPIO.IN)         #Read output from PIR motion sensor
    i = GPIO.input(gpio_motionSensor)

    if(i == 0):                	#No motion detection
        return False;
    elif(i == 1):				#motion detected
        return True;

		 

def luminositySensor():			#It needs GPIO SDA and SCL
	# Get I2C bus
	bus = smbus.SMBus(1)
	 
	bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
	bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)
	 
	time.sleep(0.5)
	data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)
	data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)
	 
	# Convert the data
	fullSpectrum = data[1] * 256 + data[0]
	infraRed = data1[1] * 256 + data1[0]
	visible = fullSpectrum - infraRed
	
	return fullSpectrum, infraRed, visible

humidity, temperature  = getHumidityTemperature()

print("Temperature: %d C" % temperature)
print("Humidity: %d %%" % humidity)