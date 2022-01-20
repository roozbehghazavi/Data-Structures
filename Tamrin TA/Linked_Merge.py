class Node: 
	def __init__(self, data): 
		self.data = data  
		self.next = None

class LinkedList:

	def __init__(self):  
		self.head = None

	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node

	def append(self, new_data): 
		new_node=Node(new_data)
		if self.head is None:
			self.head=new_node
			return
		last=self.head
		while(last.next):
			last=last.next
		last.next=new_node

	def printList(self): 
		temp = self.head 
		while (temp): 
			myList.append(temp.data)
			temp = temp.next 
	
	def mergeSort(self, head):
		if head == None or head.next== None:
			return head

		mid = self.Getmiddle(head)
		Mid = mid.next

		mid.next = None

		left = self.mergeSort(head)
		
		right = self.mergeSort(Mid)
		
		res = self.merge(left, right)
		self.printArray(res)
		return res


	def merge(self, leftSub, rightSub):
		if leftSub == None: return rightSub
		if rightSub == None: return leftSub

		res = None

		if leftSub.data <= rightSub.data:
			res = leftSub
			res.next = self.merge(leftSub.next, rightSub)
		else:
			res = rightSub
			res.next= self.merge(leftSub, rightSub.next)       
		return res 
		
	def Getmiddle(self, head):

		if(head== None):
			return head

		mid = head
		end = head

		while(end.next!= None and end.next.next != None):
			mid = mid.next
			end = end.next.next

		return mid 

	def printArray(self, headRef):
		if headRef == None: 
			print(' ')
			return
		node = headRef
		while node:
			if node.next!= None:
				print(node.data, end="->")  
			else:  
				print(node.data)  
			node = node.next

# def mergeSort(myList):
# 	if len(myList) > 1:
# 		mid = len(myList) // 2
# 		left = myList[:mid]
# 		right = myList[mid:]

# 		mergeSort(left)
# 		mergeSort(right)

# 		if(len(right)>1 and len(left)>1):
# 			for i in range(len(left)):
# 				print(str(left[i]),end="")

# 				if(i!=(len(left)-1)):
# 					print("->",end="")
# 				if(i==len(left)-1):
# 					print()

# 			for j in range(len(right)):
# 				print(str(right[j]),end="")
				
# 				if(j!=(len(right)-1)):
# 					print("->",end="")
# 				if(j==len(right)-1):
# 					print()
				
# 		i = 0
# 		j = 0
# 		k = 0
		
# 		while i < len(left) and j < len(right):
# 			if left[i] < right[j]:
# 			  myList[k] = left[i]
# 			  i += 1
# 			else:
# 				myList[k] = right[j]
# 				j += 1
# 			k += 1
# 		while i < len(left):
# 			myList[k] = left[i]
# 			i += 1
# 			k += 1

# 		while j < len(right):
# 			myList[k]=right[j]
# 			j += 1
# 			k += 1


# inp=input()
# inpdata=inp.split('->')

data = list(map(int, input().split('->')))
smp = LinkedList()
for i in range(len(data)):
	smp.append(data[i])
smp.head = smp.mergeSort(smp.head) 

# for n in range(len(inpdata)):
# 	inpdata[n]=int(inpdata[n])


# myList=inpdata
# mydata = LinkedList()  
# mydata.printList() 

# mergeSort(myList)


# for k in range(len(myList)):

# 	print(str(myList[k]),end="")	
# 	if(k!=(len(myList)-1)):
# 		print("->",end="")




