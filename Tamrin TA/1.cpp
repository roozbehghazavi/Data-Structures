#include <bits/stdc++.h> 
using namespace std; 

enum Color {WHITE, GRAY, BLACK}; 

class Graph 
{ 
	int V; // No. of vertices 
	list<int>* adj; // adjacency lists 

	bool DFSUtil(int v, int color[]); 
public: 
	Graph(int V); // Constructor 
	void addEdge(int v, int w); 

	bool isCyclic(); 
}; 

Graph::Graph(int V) 
{ 
	this->V = V; 
	adj = new list<int>[V]; 
} 

void Graph::addEdge(int v, int w) 
{ 
	adj[v].push_back(w);  
} 

bool Graph::DFSUtil(int u, int color[]) 
{ 

	color[u] = GRAY; 

	list<int>::iterator i; 
	for (i = adj[u].begin(); i != adj[u].end(); ++i) 
	{ 
		int v = *i; 


		if (color[v] == GRAY) 
		return true; 

		if (color[v] == WHITE && DFSUtil(v, color)) 
		return true; 
	} 


	color[u] = BLACK; 

	return false; 
} 
 
bool Graph::isCyclic() 
{ 
	int *color = new int[V]; 
	for (int i = 0; i < V; i++) 
		color[i] = WHITE; 

	for (int i = 0; i < V; i++) 
		if (color[i] == WHITE) 
		if (DFSUtil(i, color) == true) 
			return true; 

	return false; 
} 
 
int main() 
{ 
    int n,a,b;
    cin>>n;
    
	Graph g(n); 
	for(int i=0;i<n;i++)
	{
	    cin >> a >> b;
	    g.addEdge(a, b);
	}

	if (g.isCyclic()) 
		cout <<"1"; 
	else
		cout << "0"; 

	return 0; 
} 
