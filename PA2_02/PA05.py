from heapq import heappush, heappop
def read_file(name_file):
    graph={}
    f=open(name_file)
    fil=f.read().splitlines()
    for line in fil:
        st=line.split()  
        d={}
        for item in st[1:]:
            element=item.split(',')
            d[int(element[0])]=int(element[1])
        graph[int(st[0])]=d    
    return graph

def dijkstra(graph, start_node):
    inf = float('inf')
    dist, path, heap, visited = {start_node:0}, {}, [(0,start_node)], set() 
    while heap:
        _, u = heappop(heap)
        if u in visited: continue 
        visited.add(u) 
        for v in graph[u]: 
            new_distance = dist.get(u,inf) + graph[u][v] 
            if new_distance < dist.get(v,inf):
                dist[v], path[v] = new_distance, u 
            heappush(heap, (dist[v], v)) 
    return dist, path
        
if __name__=='__main__':
    name='C:\\Algorithms_2\\PA05\\dijkstraData.txt'
    graph=read_file(name)
    distance, path=dijkstra(graph, 1)
    print(distance[7],',',distance[37],',',distance[59],',',distance[82],',',
          distance[99],',',distance[115],',',distance[133],',',distance[165],',',
          distance[188],',',distance[197])
    
