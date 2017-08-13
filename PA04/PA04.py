# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:53:39 2017

@author: aguka
"""

def read_file():
    graph={}
    revers_graph={}
    with open('C:\\Study\\Algorithms\\PA04\\assignment_4.txt') as input_file:
        for line in input_file:
            from_v, in_v = map(int, line.split())
            graph.setdefault(from_v, []).append(in_v)
            graph.setdefault(in_v, []) 
            revers_graph.setdefault(in_v, []).append(from_v)
            revers_graph.setdefault(from_v, [])
    return graph, revers_graph      

def dfs(graph, i):
    global finish_time
    global processed_nodes
    global current_source
    stack=[]
    stack.append(i)
    while stack:
        v=stack.pop()
        if not nodes[v]:
            nodes[v]=True
            leader[current_source] = leader.setdefault(current_source, 0) + 1
            stack.append(v)     
            for item in graph[v]:
                if not nodes[item]:
                    stack.append(item)  
        else:
            if v not in finish_time:
                processed_nodes=processed_nodes+1
                finish_time[v]=processed_nodes

def dfs_loop(graph):   
    global processed_nodes   #   need for 1 pass, for finishing times 
    global current_source   #   need for 2 pass, leaders
    global leader
    processed_nodes=0
    current_source=0  
    for node in graph.keys():
        nodes[node]=False
    leader={}      
    
    if len(finish_time)==0:
        rng=sorted(nodes.items(),key=lambda x: x[0], reverse=True)
    else:
        rng=sorted(finish_time.items(), key=lambda x: x[1], reverse=True)
    for i,j in rng:
        if not nodes[i]:
            current_source=i
            dfs(graph, i)
 
if __name__ == '__main__':
    graph, revers_graph = read_file()
    nodes={}
    finish_time={}     
    dfs_loop(graph)
    dfs_loop(revers_graph)
    lst=list(sorted(leader.values(),reverse=True))
    print(lst[:5])
# 

