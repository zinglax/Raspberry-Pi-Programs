from twython import Twython as tw
from twython import TwythonStreamer
from time import gmtime, strftime

# Local libraries
import endoscope

e = endoscope.Endoscope()

class Pic_Taker_Twitter(TwythonStreamer):
    ''' Twitter class for the raspberry pi'''
    consumer_key = "XJGitZ02u0wvfJ6L3WMqT1bRL"
    consumer_secret = "Oxmq1v4DqfxW8JCcoLjSnuk8vGLwr7GJAwoNA5YrSszrPtARUI"
    access_token = "403913218-y95Au89xBX6FDkjkBg95lHOPPkeJN8L0JyuJfnip"
    access_token_secret = "5siPX5Rxe3AMGhVsl9iHA6QgJpHwxeGqIRzwugRExljCx"  
    
    def on_success(self, data):
        
        if 'text' in data:
            print data['user']['screen_name']
            print data['text'].encode('utf-8')
            
            # Image name is ./twitter_images/TWITTER_USERNAME + DATE&TIME + .jpg
            image_name = "./twitter_images/" + data['user']['screen_name'] + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".jpg"
            e.takepic( image_name, False)
            
            
            # Sending back status
            t = tw(consumer_key, consumer_secret, 
                  access_token, 
                  access_token_secret)
            
            photo = open(image_name, 'rb')
            t.update_status_with_media(status='Checkout this cool image!  @' + data['user']['screen_name'], media=photo)       
            
            
            
    
    def on_error(self, status_code, data):
        print status_code
    
        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()   


if __name__=="__main__":
    
    # OhChristmasTree (twitter app) credientials Under username TimsXmasTree
    consumer_key = "XJGitZ02u0wvfJ6L3WMqT1bRL"
    consumer_secret = "Oxmq1v4DqfxW8JCcoLjSnuk8vGLwr7GJAwoNA5YrSszrPtARUI"
    access_token = "403913218-y95Au89xBX6FDkjkBg95lHOPPkeJN8L0JyuJfnip"
    access_token_secret = "5siPX5Rxe3AMGhVsl9iHA6QgJpHwxeGqIRzwugRExljCx"  
    
    # Streaming
    stream = Pic_Taker_Twitter(consumer_key,
                        consumer_secret,
                        access_token,
                        access_token_secret)
    stream.statuses.filter(track="#TakeHolidayPic")
    