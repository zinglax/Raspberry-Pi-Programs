import endoscope
import led
import ultrasonic
import time
import webcam

#e = endoscope.Endoscope()
#l = led.LED(17, "BCM")
#u = ultrasonic.UltraSonicSensor(24, 25, "BCM")


#while True:
    #distance = u.read()
    #print round(distance, 2)
    #if 20 < distance < 30:
        #l.blink(3)
        ##e.takepic("test.jpg", False)
        
    #time.sleep(.5)

c1 = webcam.Webcam(device='/dev/video0')
c2 = webcam.Webcam(device='/dev/video1')
c3 = webcam.Webcam(device='/dev/video2')

cameras = [c1,c2,c3]

for i, camera in enumerate(cameras):
    camera.takepic('/webcam_pics/camera_'+str(i)+'_image.jpg')
    
