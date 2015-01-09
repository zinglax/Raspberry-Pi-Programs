import RPi.GPIO as GPIO
import time

"""
Author: Dylan Zingler
Date: 1/8/15
Description: Class Object for a RGB LED
"""

class RGBled:
    '''A class for a single RGB LED wired to the pi'''
    r_pin = None
    g_pin = None
    b_pin = None
    
    def __init__(self, r_pin, b_pin, g_pin, pin_type):
        self.r_pin = r_pin
        self.g_pin = g_pin
        self.b_pin = b_pin
        
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
        GPIO.setup(r_pin, GPIO.OUT)
        GPIO.setup(g_pin, GPIO.OUT)
        GPIO.setup(b_pin, GPIO.OUT)
        
    def blink_r(self, seconds):
        self.on_r()
        time.sleep(seconds/2)
        self.off_r()
        time.sleep(seconds/2)  
        
    def blink_g(self, seconds):
            self.on_g()
            time.sleep(seconds/2)
            self.off_g()
            time.sleep(seconds/2)              

    def blink_b(self, seconds):
            self.on_b()
            time.sleep(seconds/2)
            self.off_b()
            time.sleep(seconds/2)          

    def on_r(self):
        GPIO.output(self.r_pin, GPIO.HIGH)

    def off_r(self):
        GPIO.output(self.r_pin, GPIO.LOW)

    def on_g(self):
        GPIO.output(self.g_pin, GPIO.HIGH)

    def off_g(self):
        GPIO.output(self.g_pin, GPIO.LOW)

    def on_b(self):
        GPIO.output(self.b_pin, GPIO.HIGH)

    def off_b(self):
        GPIO.output(self.b_pin, GPIO.LOW)
                
if __name__=="__main__":
    led = RGBled(24, 18, 23, "BCM")
    
    for i in range(0,25):
        led.blink_r(.2)
        led.blink_g(.2)
        led.blink_b(.2)