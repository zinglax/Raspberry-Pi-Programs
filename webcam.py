import subprocess

class Webcam:
    ''' Class for Webcam '''
    resolution = "640x480"
    device = '/dev/video0'
        
    def __init__(self, **kwargs):
        ''' Sets all attributes passed to class values'''
        for key, value in kwargs.items():
            setattr(self, key, value)      
    
    def takepic(self, file_and_path, banner=True):
        ''' Takes a picture given a specified name, command should look like
        fswebcam -r 640x480 --no-banner image3.jpg        
        or something similar '''        
        command = "fswebcam -r " + self.resolution + " -d " + self.device + ' '
        
        # check to add banner
        if banner == False:
            command += "--no-banner "
        
        # adds the file path
        command += file_and_path
        
        print command
        
        return_val = subprocess.call(command, shell=True)
        
        if return_val == 0:
            print "picture taken!!!"
        else:
            print "oops the picture was not taken :-("
        
        
if __name__=="__main__":
    
    camera = Webcam(resolution="640x480")
    camera.takepic("py_program_image.jpg", banner=False)
    