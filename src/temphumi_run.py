import sys
import time
import Adafruit_DHT
#from dynamodb_json import json_util as json
#Config pin :
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

#Config temps :
time_start = time.time()

#Config save :
fichier = open("temphumiint.txt", "w")

#Loop :
try:
    while True:
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

        #Affichage / Sauvegarde des donnees :
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            current_time = time.time() - time_start
            fichier.write(str(int(current_time))) #arrondi du temps sur un int
            fichier.write(' seconds : Temp={0:0.1f}*  Humidity={1:0.1f}% \n'.format(temperature, humidity))
            
#            json_ = {"Time": current_time,
#            "Temperature": temperature,
#           "Humidity": humidity,
#            }
            
        else:
            print('Failed to get reading. Try again!')
            sys.exit(1)
            
        #Temps de pause :
        time.sleep(10) #toutes les minutes

#Fermeture :
except KeyboardInterrupt:
    print (" Quit")
    fichier.close()
    GPIO.cleanup()










#dynamodb_json = json.dumps(json_)

# {
# "my_dict": {"M": {"my_date": {"S": "2017-04-22T14:41:35.780000"}}}, 
# "MyBool": {"BOOL": false}, "MyNone": {"NULL": true}, 
# "MyNestedDict": {
# "M": {"my_other_nested": {
# "M": {"myUUID": {"S": "2f4ad21e098f49b18e22ad209779048b"}, 
# "surname": {"S": "Lennon"}, "name": {"S": "John"}, 
# "mySet": {"L": [{"N": "1"}, {"N": "3"}, {"N": "4"}, {"N": "5"}, {"N": "6"}]}, 
# "floaty": {"N": "29.4"}, "time": {"N": "1492872095.78"}, 
# "myList": {"L": [{"N": "1"}, {"N": "3"}, {"N": "4"}, {"N": "5"}, {"N": "6"}, {"S": "This Is Sparta!"}]}, 
# "MyOtherNone": {"NULL": true}}
# }
# }
# }, 
# "myDecimal": {"N": "19.2"}, "num": {"N": "4"}, 
# "MyString": {"S": "a"}, 
# "myLong": {"N": "1938475658493"}, 
# "MyZero": {"N": "0"}
# }


#json.loads(dynamodb_json)

# {'my_dict': {'my_date': datetime.datetime(2017, 4, 22, 14, 41, 35, 780000)}, 'MyBool': False, 'MyNone': None,
# 'MyNestedDict': {
# 'my_other_nested': {'myUUID': '2f4ad21e098f49b18e22ad209779048b', 
# 'surname': 'Lennon', 'name': 'John',
# 'mySet': [1, 3, 4, 5, 6], 
# 'floaty': 29.4, 
# 'time': 1492872095.78,
# 'myList': [1, 3, 4, 5, 6, 'This Is Sparta!'], 
# 'MyOtherNone': None
# }
# }, 
# 'myDecimal': 19.2,
# 'num': 4, 
# 'MyString': 'a', 
# 'myLong': 1938475658493L, 
# 'MyZero': 0
# }
    
