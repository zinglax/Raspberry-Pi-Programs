import RPi.GPIO as GPIO
import time

"""
Author: Dylan Zingler
Date: 1/4/15
Description: Library for using Passive Infrared Sensor HC-SR501
with a Raspberry Pi. 
"""

class PassiveInfraredSensor:
    ''' A class for a single Passive Infrared Sensor'''
    outputpin = None
    pin_type = "BCM"
    
    def __init__(self, outputpin, pin_type):
        self.outputpin = outputpin
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
            
        # Setting up pins
        GPIO.setup(outputpin, GPIO.IN)
        time.sleep(0.3)
        
        
    def read(self):
        "gets a reading from sensor"
        return GPIO.input(self.outputpin)
    
    def passiveinfrared_generator(self, time_delay, num_readings):
        '''Generator for getting multiple readings over a period of time'''
        for i in range(num_readings):
            yield self.read()
            time.sleep(time_delay)
            
if __name__=="__main__":
    # Creating a Passive Infrared Sensor object
    pir = PassiveInfraredSensor(18, "BCM")
    
    # Create Generator
    twentyValues = pir.passiveinfrared_generator(0.5, 20)
    for i in twentyValues:
        if i == 0:
            print "Nothing Detected..."
        else:
            print "Sensor Detected Something!"
    
            