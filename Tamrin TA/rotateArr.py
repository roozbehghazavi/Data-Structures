# O(N):
def rotateArr1(array,length,rotation):
    for i in range(rotation):
        array.append(array.pop(0))
    print(*array)

# O(N*d):
def rotateArr2(array,length,rotation):
    for i in range(rotation):
        temp=array[0]
        for j in range(length-1):
            array[j]=array[j+1]
        array[length-1]=temp

    for k in range(len(array)):
        print(array[k],end=" ")


data=input()
L=int(input())
data=list(map(int, data.split()))
rotateArr1(data,len(data),L)