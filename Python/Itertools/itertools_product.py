# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
P=list(product(A,B))
for i in range(len(P)):
    print(P[i],end=" ")
