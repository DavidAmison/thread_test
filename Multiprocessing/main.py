"""
Created on Wed Mar 15 15:26:00 2017

Code for testing multi-threading on the Raspberry pi

@author: David
"""

from test_thread import testProcess
import timeit

if __name__ == '__main__':
    process_1 = testProcess(1,'process_1',20000)
    process_2 = testProcess(2,'process_2',20000)
    
    start_time = timeit.default_timer()
    process_1.start()
    #process_1.join()
    process_2.start()
    process_2.join()
    elapsed_time = timeit.default_timer() - start_time
    print('Total Time:' + str(elapsed_time))

