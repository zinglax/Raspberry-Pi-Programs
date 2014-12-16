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
    trigger = None
    echo = None
    pin_type = "BCM"
    
    def __init__(self, trigger, echo, pin_type):
        self.trigger = trigger
        self.echo = echo
        self.pin_type = pin_type
        
        # No GPIO Warnings
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
        GPIO.setup(trigger, GPIO.OUT) 	# Trig = GPIO.OUT
        GPIO.setup(echo, GPIO.IN)	# Echo = GPIO.IN
        GPIO.setup(trigger, GPIO.LOW)                
        time.sleep(0.3)

    def read(self):
        ''' Get a single reading from the ultrasonic sensor'''
        
        # Send 1 microsignal from trigger
        GPIO.output(self.trigger, True)    
        time.sleep(0.00001)    
        GPIO.output(self.trigger, False)
    
        # Not Recieving, start time
        while GPIO.input(self.echo) == 0:
            signaloff = time.time()
    
        # Signal recieved, stop time
        while GPIO.input(self.echo) == 1:
            signalon = time.time()
    
        # Calculate difference in time and then convert to centemeters
        timepassed = signalon - signaloff    
        distance = timepassed * 17000
        return distance    
            
    def ultrasonic_generator(self, time_delay, num_readings):
        '''Generator for getting multiple readings over a time period'''
        for i in range(num_readings):
            yield self.read()
            time.sleep(time_delay)                    
            
if __name__== "__main__": 

    # Creates Ultrasonic Sensor Object
    sensor1 = UltraSonicSensor(24, 25, "BCM")    
    
    # Creates Generator for 5 values taken a half second apart
    fiveValues = sensor1.ultrasonic_generator(0.5, 5)
    for i in fiveValues:
        print "Distance: " + str(round(i,2))+ "cm"