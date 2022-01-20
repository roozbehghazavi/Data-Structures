class Tree:
    def __init__(self,n,data):
        self.n=n
        self.data=data
        
    def Height(self,parent, index , h): 
        if(h[index]!=0): 
            return 0 
        
        if(parent[index]==-1): 
            h[index] = 1
            return 0
    
        if(h[parent[index]] == 0): 
            Tree.Height(self,parent, parent[index] , h) 
    
        h[index] = h[parent[index]] + 1
    
    def Find_Height(self,parent): 
        n = len(parent)   
        h = [0 for i in range(n)] 
    
        for i in range(n): 
           Tree.Height(self,parent, i, h) 
    
        height2 = h[0] 
        for i in range(1,n): 
            height2 = max(height2, h[i]) 
    
        return height2 
   

n=int(input())
data=input()
data=list(map(int, data.split()))

if(len(data)!=n):
    quit()

tr=Tree(n,data)
print(tr.Find_Height(data)) 
  