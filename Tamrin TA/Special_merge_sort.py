def Merge_Sort(array):
	if len(array) > 1:
		mid = len(array)//2

		Left = array[:mid]
		Left.sort(reverse=True)

		Right = array[mid:]
		Right.sort(reverse=True)

		
		Merge_Sort(Left)
		Merge_Sort(Right)

		i = j = k = 0

		while i < len(Left) and j < len(Right):
			if Left[i] < Right[j]:
				array[k] = Left[i]
				i += 1
			else:
				array[k] = Right[j]
				j += 1
			k += 1

		while i < len(Left):
			array[k] = Left[i]
			i += 1
			k += 1

		while j < len(Right):
			array[k] = Right[j]
			j += 1
			k += 1

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

FinalData=[]
data=input()
data=list(map(int, data.split()))

Merge_Sort(data)
data.reverse()
for i in range(len(data)):
	if(isPrime(data[i])==False):
		FinalData.append(data[i])
		
print(*FinalData)





