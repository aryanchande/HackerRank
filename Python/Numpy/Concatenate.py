import numpy as np 
n,m,p=map(int,input().split())
r=[]
c=[]
for i in range(n):
    e=list(map(int,input().split()))
    r.append(e)
for i in range(m):
    e=list(map(int,input().split()))
    c.append(e)
a1=np.array(r) 
a2=np.array(c)
print(np.concatenate((a1,a2)))