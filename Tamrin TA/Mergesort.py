def mergeSort(myList):
	if len(myList) > 1:
		mid = len(myList) // 2
		left = myList[:mid]
		right = myList[mid:]

		# Recursive call on each half
		mergeSort(left)
		mergeSort(right)

		if(len(right)>1 and len(left)>1):
			print()
			for i in range(len(left)):
				print(str(left[i]),end="")

				if(i!=(len(left)-1)):
					print("->",end="")

			print("")

			for j in range(len(right)):
				print(str(right[j]),end="")
				
				if(j!=(len(right)-1)):
					print("->",end="")
				
		
		# Two iterators for traversing the two halves
		i = 0
		j = 0
		
		# Iterator for the main list
		k = 0
		
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
			  # The value from the left half has been used
			  myList[k] = left[i]
			  # Move the iterator forward
			  i += 1
			else:
				myList[k] = right[j]
				j += 1
			# Move to the next slot
			k += 1

		# For all the remaining values
		while i < len(left):
			myList[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			myList[k]=right[j]
			j += 1
			k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print()
for k in range(len(myList)):
	print(str(myList[k]),end="")
				
	if(k!=(len(myList)-1)):
		print("->",end="")