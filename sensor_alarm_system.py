'''
***RASPBERRY PI PROJECT***
Sensor Alarm Systems (SAS)

Author: Dylan Zingler
Purpose: To notify recipiant of sensor detecting opened or closed door via Twitter posts
Components: RGB-LED, Ultrasonic Sensor or PIR Sensor
-
'''

from twython import Twython as tw
from twython import TwythonStreamer
from time import gmtime, strftime
import time


# Local libraries
import endoscope
import ultrasonic
import RGBled

class SensorAlarmSystem(TwythonStreamer):
    consumer_key = "XJGitZ02u0wvfJ6L3WMqT1bRL"
    consumer_secret = "Oxmq1v4DqfxW8JCcoLjSnuk8vGLwr7GJAwoNA5YrSszrPtARUI"
    access_token = "403913218-y95Au89xBX6FDkjkBg95lHOPPkeJN8L0JyuJfnip"
    access_token_secret = "5siPX5Rxe3AMGhVsl9iHA6QgJpHwxeGqIRzwugRExljCx"    
    
    on_off = False


    def take_picture_send_tweet(self, data, twythonObj):
        e = endoscope.Endoscope()        
        
        # Image name is ./twitter_images/TWITTER_USERNAME + DATE&TIME + .jpg
        image_name = "./twitter_images/" + data['user']['screen_name'] + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".jpg"
        e.takepic( image_name, False)            

        photo = open(image_name, 'rb')
        twythonObj.update_status_with_media(status='Checkout this cool image!  @' + data['user']['screen_name'], media=photo)        
        
    def start_ultrasonic_sensor(self):
        distance = 50
        
        u = ultrasonic.UltraSonicSensor(22,17,"BCM")
        l = RGBled.RGBled(23, 18, 24, "BCM")
        
        l.on_b()
        print "blue led is now on"
                
        x= u.read()
        while x <= 50:
            l.blink_r(1)
            x = u.read()
            time.sleep(0.5)
            
            
        print "sensor now reads greater than 50"
        l.blink_g(5)
        l.off_b()
        l.on_g()
        
        
    def on_success(self, data):
        
        if 'text' in data:
            print data['user']['screen_name']
            print data['text'].encode('utf-8') 

            # Twython Interaction
            t = tw(consumer_key, consumer_secret, 
                  access_token, 
                  access_token_secret)
            
            # Do something With sensors, send a tweet back maybe
            #    Honestly its up to you. Play it cool.
            
            # Is your USB camera Setup?
            # self.take_picture_send_tweet(data, t)
            
            self.start_ultrasonic_sensor()
            
            print "WOW WHAT A GREAT DAY"
            
            
            

if __name__=="__main__":
    # OhChristmasTree (twitter app) credientials Under username TimsXmasTree
    consumer_key = "XJGitZ02u0wvfJ6L3WMqT1bRL"
    consumer_secret = "Oxmq1v4DqfxW8JCcoLjSnuk8vGLwr7GJAwoNA5YrSszrPtARUI"
    access_token = "403913218-y95Au89xBX6FDkjkBg95lHOPPkeJN8L0JyuJfnip"
    access_token_secret = "5siPX5Rxe3AMGhVsl9iHA6QgJpHwxeGqIRzwugRExljCx"  
    
    # Streaming
    stream = SensorAlarmSystem(consumer_key,
                               consumer_secret,
                               access_token,
                               access_token_secret)
    stream.statuses.filter(track="#OONN")    
