"""
Created on Wed Mar 15 15:26:00 2017

Code for testing multi-threading on the Raspberry pi

@author: David
"""

import os
from pathlib import Path
from test_thread import testThread

f = Path(os.path.dirname(__file__)) / 'test.txt'
thread_1 = testThread(1,'thread_1',f)
thread_2 = testThread(2,'thread_2',f)


thread_1.start()
thread_2.start()

