"""
Created on Wed Mar 15 15:27:04 2017
Test Thread class for the rasppeery pi
@author: David
"""

import threading
from pathlib import Path
import timeit

class testThread(threading.Thread):
    
    def __init__(self, threadID, name, file):
        threading.Thread.__init__(self)
        self.ID = threadID
        self.name = name
        self.file = file
    
    def run(self):
        start_time = timeit.default_timer()
        #open file for reading
        f = open(str(self.file),'r')
        #read the file and print to the command line
        for line in f:
            print(self.name + ':' + line)
        elapsed_time = timeit.default_timer() - start_time
        print(self.name + ':' + str(elapsed_time))
        return
        