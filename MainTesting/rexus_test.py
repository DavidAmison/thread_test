"""
Created on Fri Mar 17 16:49:16 2017


@author: David
"""
import multiprocessing
from IMUProcess import IMUProcess
from PiCam import PiCam
import timeit

if __name__ = '__main__':
    
    st = timeit.default_timer()
    p_1 = IMUProcess()
    p_2 = PiCam()
    
    p_1.start()
    p_2.start()
    
    p_1.join()
    p_2.join()
    
    tm = timeit.default_timer() - st
    print('Total Time:',tm,'s')