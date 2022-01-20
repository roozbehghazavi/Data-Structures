from bigO import bigO
from random import randint

def example(n):
    for i in range(1,n):
        for j in range(1,n):
            print("bakhshande")


tester = bigO()
complexity= tester.test(example,"random")
print(complexity)