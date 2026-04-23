import numpy as np
n,m=map(int,input().split())
a=[]
for i in range(n):
    e=list(map(int,input().split()))
    a.append(e)
arr=np.array(a)
print(np.transpose(arr))
print(arr.flatten())