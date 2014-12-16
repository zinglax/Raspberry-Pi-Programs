import RPi.GPIO as GPIO
import time

"""
Author: Dylan Zingler
Date: 12/15/14
Description: Library for using Ultrasonic Module HC-SR04
with a Raspberry Pi. Code was modeled off of
http://www.bytecreation.com/blog/2013/10/13/raspberry-pi-ultrasonic-sensor-hc-sr04"""

class UltraSonicSensor:
    '''A class for a single Ultra Sonic Sensor'''
    
    def __init__(self, trigger, echo, pin_type):
        self.trigger = trigger
        self.echo = echo
        self.pin_type = pin_type
        
        GPIO.setwarnings(False)
        
        if pin_type in  {"BOARD", "Board", "board"}:            
            # Sets up GPIO, BOARD for actual Pin numbers
            GPIO.setmode(GPIO.BOARD)
        elif pin_type in {"BCM", "bcm"}:
            # BCM for GPIO numbers (labeled on Cobbler)
            GPIO.setmode(GPIO.BCM)
        else:
            print "Did not understand pin type, setting to GPIO.BCM"
            GPIO.setmode(GPIO.BCM)
        
        # Setting up trigger and echo pins            
        GPIO.setup(trig, GPIO.OUT) 	# Trig = GPIO.OUT
        GPIO.setup(echo, GPIO.IN)	# Echo = GPIO.IN
        GPIO.setup(trig, GPIO.LOW)        
        
        time.sleep(0.3)

    def read(self):
        ''' Get a single reading from the ultrasonic sensor
        code taken from'''
    
        GPIO.output(trig, True)
    
        time.sleep(0.00001)
    
        GPIO.output(trig, False)
    
        while GPIO.input(echo) == 0:
            signaloff = time.time()
    
        while GPIO.input(echo) == 1:
            signalon = time.time()
    
        timepassed = signalon - signaloff
    
        distance = timepassed * 17000
    
        return distance
    
            
    def ultrasonic_generator(self, time_delay, num_readings):
        '''Generator for getting a list of values'''
        for i in range(num_readings):
            yield read(self)
            time.sleep(time_delay)        
            
if __name__== "__main__": 
    
    sensor1 = UltraSonicSensor(24, 25, "BCM")    
    print sensor1.read()