import RPi.GPIO as GPIO
import time

'''
pins = [7,13,15,16]

for p in pins:    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, False)
'''

def reading(sensor, trig, echo):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    if sensor == 0:
        GPIO.setup(trig, GPIO.OUT) 	# Trig = GPIO.OUT
        GPIO.setup(echo, GPIO.IN)	# Echo = GPIO.IN
        GPIO.setup(trig, GPIO.LOW)

        time.sleep(0.3)

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

        GPIO.cleanup()

    else:	
        print "Incorrect usonic() function variable."



t = 12 # trigger
e = 11 # echo

while True:
    print reading(0, t, e)
    time.sleep(.35)