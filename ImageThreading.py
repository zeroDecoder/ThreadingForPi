import numpy as np
import cv2
import time
import multiprocessing
import math
import time
from threading import Thread
from Queue import Queue

cannyImages = []
mainQueue = Queue()

def processImage():
	idleTime = time.time()
	while(time.time() - idleTime < 0.1 or not mainQueue.empty()): #exits after timeout unless thread still has data to process
		if(mainQueue.qsize() > 0): #unsafe method. if another thread pops data after this line and the queue is empty program will hang.
			print(mainQueue.get())

	



#Main Program Start 
thread1 = Thread(target=processImage, args=())
thread1.start()

x=0
while x<500:
	mainQueue.put('lol');
	x=x+1
thread1.join()


