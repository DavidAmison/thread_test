"""
Created on Fri Mar 17 16:49:16 2017


@author: David
"""

import IMU
import timeit

start = timeit.default_timer()
IMU.collect_date(10)
length = timeit.default_timer() - start
print('collecting data took:',length,'s')