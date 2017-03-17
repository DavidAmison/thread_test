"""
Created on Fri Mar 17 16:49:16 2017


@author: David
"""
import timeit
import IMU
import multiprocessing

class IMUProcess(multiprocessing.Process):
    
    def run(self):
        st = timeit.default_timer()
        IMU.collect_data(100)
        tm = timeit.default_timer() - st
        print('IMU took:',tm,'s')