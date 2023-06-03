import RPi.GPIO as GPIO
import Adafruit_DHT
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
fan_pin = 36

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(fan_pin,GPIO.OUT)
    return()
    
def fanON():
    setPin(True)
    return()
    
def fanOFF():
    setPin(False)
    return()
    
def setPin(mode):
    GPIO.output(fan_pin, mode)
    return()

try:
    setup()
    while 1:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        
        if(temperature > 28 and temperature is not None):
            print("Temp={0:0.1f}C".format(temperature))
            fanON()
            print("Fan ON")
            time.sleep(5)
        else:
            fanOFF()
            print("Fan Off")
            time.sleep(1)
        
        time.sleep(1)
        
except KeyboardInterrupt:
	GPIO.cleanup()