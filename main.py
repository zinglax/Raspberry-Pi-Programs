import endoscope
import led
import ultrasonic
import time
import webcam
import RGBled

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

#c1 = webcam.Webcam(device='/dev/video0')
#c2 = webcam.Webcam(device='/dev/video1')
#c3 = webcam.Webcam(device='/dev/video2')

#cameras = [c1,c2,c3]

#for i, camera in enumerate(cameras):
    #camera.takepic('/webcam_pics/camera_'+str(i)+'_image.jpg')


u = UltraSonicSensor(22, 17, "BCM")    
l = RGBled.RGBled(23, 18, 24, "BCM")

while True:
    
    num_dist_reads = 9
    door_open_avg = 140
    door_closed_avg = 135
    
    reads = u.ultrasonic_generator(.2,num_dist_reads)
    for d in reads:
        total += d 
    
    avg = total/num_dist_reads
    if avg > 140:
        # Door Open
        l.on_b()
        l.blink_r(5)
        l.off_b()
        
    else:
        # Door Closed
        l.on_g()
        time.sleep(5)
        l.off_g()