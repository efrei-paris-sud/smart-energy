import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

#Config temps :
time_start = time.time()

#Config save :
fichier = open("tempext.txt", "w")
try:
    while True:
        temperature = sensor.get_temperature()
        current_time = time.time() - time_start
        fichier.write(str(int(current_time))) #arrondi du temps sur un int
        fichier.write(' seconds : ' + str(temperature)+ '\n')
        
        print('the temperature is %s celsius' %temperature)
        time.sleep(1)
#Fermeture :
except KeyboardInterrupt:
    print (" Quit")
    fichier.close()
