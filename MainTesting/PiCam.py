"""
Created on Fri Mar 17 16:49:16 2017


@author: David
"""

import picamera
import multiprocessing

class PiCam(multiprocessing.Process):
    
    def run(self):
        camera = picamera.PiCamera(resolution=(640, 480))
        camera.start_recording('1.h264')
        camera.wait_recording(5)
        for i in range(2, 11):
            camera.split_recording('%d.h264' % i)
            camera.wait_recording(5)
        camera.stop_recording()