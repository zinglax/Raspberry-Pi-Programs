import endoscope
import led
import ultrasonic
import time

#e = endoscope.Endoscope()
l = led.LED(17, "BCM")
u = ultrasonic.UltraSonicSensor(24, 25, "BCM")


while True:
    distance = u.read()
    print round(distance, 2)
    if 20 < distance < 30:
        l.blink(3)
        #e.takepic("test.jpg", False)
        
    time.sleep(.5)
