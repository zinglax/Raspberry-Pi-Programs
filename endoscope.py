import subprocess

class Endoscope:
    ''' Class for Endoscope webcam'''
    resolution = "640x480"
        
    def __init__(self, resolution="640x480"):
        self.resolution = resolution
    
    def takepic(self, file_and_path, banner=True):
        ''' Takes a picture given a specified name, command should look like
        fswebcam -r 640x480 --no-banner image3.jpg        
        or something similar '''        
        command = "fswebcam -r " + self.resolution + " "
        
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
    
    camera = Endoscope("640x480")
    camera.takepic("py_program_image.jpg", banner=False)
    