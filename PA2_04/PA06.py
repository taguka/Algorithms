# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:19:19 2017

@author: ur00656
"""
import time

def read_file(name):
    f=open(name,'r')
    input_data=f.read().splitlines()
    return list(map(int,input_data))

def load_hashtable(array):
    hash_table={}
    for i, element in enumerate(array):
        hash_table[element]=i
    return hash_table

if __name__=='__main__':  
    array=read_file('C:\\Algorithms_2\\PA06\\assignment_6-1.txt')   
    start_time = time.time()
    cn=0
    H=load_hashtable(array)
    print("--- %s seconds ---" % (time.time() - start_time))

    for num in range(-10000,10001):
        if num%1000==0:
            print(num)
        for x in array:
            if H.get((num-x),None)!= None:
                cn=cn+1
                break
    print(cn)    
    print("--- %s seconds ---" % (time.time() - start_time))



 
            