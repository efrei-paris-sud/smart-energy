import os
import glob
import time
import subprocess

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '')[0]
device_file = device_folder + '/w1_master_slaves'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
#    catdata = subprocess.Popen(['cat', device_file], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
#    out,err = catdata.communicate()
#    out_decode= out.decode('utf-8')
#    lines = out_decode.split('\n')
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
    
    
    
    
#Config temps :
time_start = time.time()

#Config save :
fichier = open("tempext.txt", "w")

#Loop :
try:
    while True:
            current_time = time.time() - time_start
            data = read_temp()
            print(data)
            fichier.write(str(int(current_time))) #arrondi du temps sur un int
            fichier.write(' seconds : ' + str(data)+ '\n')
            time.sleep(10) #chaque minute
#Fermeture :
except KeyboardInterrupt:
    print (" Quit")
    fichier.close()


            
