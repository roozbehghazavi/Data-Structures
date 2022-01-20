from collections import defaultdict 
  
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
        visited[v] = True
        recStack[v] = True
   
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True
  
        recStack[v] = False
        return False

    def isCyclic(self): 
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False

edge_count=int(input()) 
G=Graph(edge_count)

for i in range(edge_count):
    data=input()
    data=list(map(int, data.split()))
    G.addEdge(data[0],data[1])
    data.clear()



if G.isCyclic() == 1: 
    print (1)
else: 
    print (0)
  
