# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:49:06 2017

@author: ur00656
"""
import time
from  heapq import heappush, heappop
def read_file(name):
    arr=[]
    with open(name,'r') as file:
        for line in file:
            arr.append(int(line))
    return arr    

def median(array):
    heap_min, heap_max=[],[] 
    heappush(heap_min, array[0])
    cn=array[0] 
    for i, val in enumerate(array[1:]):
        if val>heap_min[0]:
            heappush(heap_min, val)
        else:
            heappush(heap_max, -val)
        if (len(heap_min)>len(heap_max)) or ((i%2==1) and len(heap_min)==len(heap_max)):
            ins=heappop(heap_min)
            heappush(heap_max,-ins)
        else:
            if ((i%2==0) and len(heap_min)<len(heap_max)):
                ins=heappop(heap_max)
                heappush(heap_min,-ins)
        cn=cn-heap_max[0]    
    return  cn%10000

        
if __name__=='__main__':
        avg_time=0
        array=read_file('C:\\Algorithms_2\\PA2_03\\Median.txt')
        start_time=time.time()
        for i in range(100):
            t=median(array)
        print((time.time() - start_time))
#9335