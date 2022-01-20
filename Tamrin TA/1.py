from collections import defaultdict 

class Graph(): 
	def __init__(self, V): 
		self.V = V 
		self.graph = defaultdict(list) 

	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	def DFSUtil(self, u, color): 
		color[u] = "GRAY"
		for v in self.graph[u]: 

			if color[v] == "GRAY": 
				return True

			if color[v] == "WHITE" and self.DFSUtil(v, color) == True: 
				return True

		color[u] = "BLACK"
		return False

	def isCyclic(self): 
		color = ["WHITE"] * self.V 

		for i in range(self.V): 
			if color[i] == "WHITE": 
				if self.DFSUtil(i, color) == True: 
					return True
		return False

edge_count=int(input()) 
g=Graph(edge_count)

for i in range(edge_count):
    data=input()
    data=list(map(int, data.split()))
    g.addEdge(data[0],data[1])
    data.clear()

if(g.isCyclic() == True):
    print(1)
else:
    print(0)
							
