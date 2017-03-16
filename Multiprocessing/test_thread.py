"""
Created on Wed Mar 15 15:27:04 2017
Processor class for the rasppeery pi calculating prime numbers
@author: David
"""

import multiprocessing
import timeit

class testProcess(multiprocessing.Process):
    
    def __init__(self, threadID, name, n):
        multiprocessing.Process.__init__(self)
        self.ID = threadID
        self.name = name
        self.n = n
    
    def run(self):
        print(self.name,'Calculating primes upto', self.n)
        start_time = timeit.default_timer()
        #Calculate prime numbers upto and including n
        primes = []
        for num in range(2,self.n):
            is_prime = True
            for div in range(2,num):
                if num%div == 0:
                    is_prime = False
                    break
            if is_prime: 
                primes.append(num)
        
        elapsed_time = timeit.default_timer() - start_time
        print(self.name + ':' + str(elapsed_time),'s')
        return
        