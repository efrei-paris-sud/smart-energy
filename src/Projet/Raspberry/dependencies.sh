#Setup dependencies


#DHT sensor humidity and temperature
sudo apt-get update
sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl
sudo python setup.py install

#TSL2561 Luminosity Sensor
cd ..
git clone https://github.com/bivab/smbus-cffi.git
cd smbus-cffi
python setup.py install


