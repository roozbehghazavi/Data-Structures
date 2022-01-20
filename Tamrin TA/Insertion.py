data=input()
data=list(map(int, data.split()))

def insertionSort(array):
	data2.append(array[:])
	for step in range(1, len(array)):
		key = array[step]
		j = step - 1       
		while j >= 0 and key < array[j]:
			array[j + 1] = array[j]
			j = j - 1
		array[j + 1] = key
		if array not in data2:
			data2.append(array[:])
	data2.pop(0)
	for i in data2:
		print(*i)

data2=[]
insertionSort(data)







