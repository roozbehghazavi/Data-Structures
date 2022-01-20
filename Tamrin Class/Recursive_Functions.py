def factorial(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

def power(a,b):
    if(a==1 or b==0):
        return 1
    else:
        return a*power(a,b-1)

def char_permutation(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return n*char_permutation(n-1)

def f(n):
    if(n>0):
        print(n)
        f(n-1);
        print(n)
    
# print(factorial(4))
# print(power(1,4))
# print(char_permutation(4))
print(f(5))