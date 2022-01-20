import sys
print("Baraye inke pichidegi zamani algorithm az martabe (log n) shavad bayad az binary search estefade konim")
print("T(n) = T(n/2) + c")
print("Theta(Logn)")
print(" ")

def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2

    if elem == arr[mid]:
        All_Numbers.remove(elem)

    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    
    return binary_search_recursive(arr, elem, mid+1, end)

N=int(input("Please Enter N:"))
All_Numbers=list(range(1,N+1))


for i in range(1,N):
    nums=int(input("Please Enter The Numbers(Between 1 & N):"))
    if(nums<=0 or nums>N):
        sys.exit("The number is not between (1 & N) Please Try Again!")
        
    binary_search_recursive(list(range(1,N)),nums)


print(All_Numbers[0],"Has not been Entered")
