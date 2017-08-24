# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 11:39:16 2017

@author: ur00656
"""
#path = []
#time = 0
#finish_time_dic = {}
#for i in range(max(max(ori_data)),0,-1):
#    start = i
#    q = [start]
#    while q:
#        v = q.pop(0)
#        if v not in path:
#            path.append(v)
#            q = [v] + q
#            for w in revscc_dic[v]:
#                if w not in path: q = [w] + q
#        else:
#            if v not in finish_time_dic:
#                finish_time_dic[v] = time
#                time += 1
#print path  
#print finish_time_dic
import time
def load_graph(name):
    G=dict()
    Grev=dict()
    with open(name,'r') as f:
        lines=f.read().splitlines()
    for line in lines:
        v,u=int(line.split()[0]),int(line.split()[1])   
        G.setdefault(v, set()).add(u)
        Grev.setdefault(u, set()).add(v)
    return G, Grev
    
def dfs(G, iterator):
    time=0
    finish_time=dict()
    visited=set()
    Q=[]
    leader=dict()
    for i in iterator: 
        if i in visited:
            continue
        cn=0
        Q.append(i)        
        while Q:
            v=Q.pop()
            if v not in visited:
                visited.add(v)
                Q.append(v)
                cn=cn+1
                try:
                    for u in G[v]:
                        if u not in visited:
                            Q.append(u)
                except KeyError:
                    pass
            else:
                if v not in finish_time:
                    time+=1
                    finish_time[v]=time     
        leader[i]=cn     
    return finish_time, leader
 
def scc(G, Grev):
    list_nodes = list(range(max(G.keys()),0,-1))
    finishing_time, leader=dfs(G, list_nodes)
    list_nodes=sorted(finishing_time, key=finishing_time.get, reverse=True)
    finishing_time, leader=dfs(Grev, list_nodes)
    return leader

if __name__=='__main__':
    G, Grev =load_graph('C:\\Algorithms_2\\PA04\\scc.txt')
    res=scc(G, Grev)
    res=sorted(res.values(), reverse=True)
    lst=list(res)
    
    
 