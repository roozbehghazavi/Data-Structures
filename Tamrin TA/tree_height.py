from collections import defaultdict
import queue

def compute_height(root,tree):
	q=queue.Queue(maxsize=20)
	q.put(root)
	q.put('sign')
	height=1

	while(not q.empty()):
		elem=q.get()

		if(elem=='sign'and not q.empty()):
			elem=q.get()
			height+=1
			q.put('sign')
		for child in tree[elem]:
			q.put(child)
		
	return height

tree=defaultdict(list)

count=int(input())
data=input()
data=list(map(int, data.split()))

if(len(data)!=count):
	quit()
parents=data

for node,parent in enumerate(parents):
	tree[parent].append(node)

root=tree.pop(-1)[0]

print(compute_height(root,tree))
