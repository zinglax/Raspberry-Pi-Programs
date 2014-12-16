import RPi.GPIO as GPIO
import time

"""
Author: Dylan Zingler
Date: 12/15/14
Description: Class object for an LED. This allows easy on and off as well as blinking functionality for the LED with simple calls like led2.on() or led5.blink()"""

class LED:
    ''' A class for a single LED wired to the pi'''
    pin = None
    
    def __init__(self, pin, pin_type):
        self.pin = pin
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
    
        # Setting up pin for output
        GPIO.setup(pin, GPIO.OUT)
        
    def blink(self, seconds):
        self.on()
        time.sleep(seconds/2)
        self.off()
        time.sleep(seconds/2)
        
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        
if __name__=="__main__":
    led = LED(17,"BCM")
    
    for i in range(0,25):
        led.blink(.2)
    