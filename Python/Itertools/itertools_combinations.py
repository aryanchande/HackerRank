# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
st,k=input().split()
st=sorted(st)
ik=int(k)
for i in range(1,ik+1):
    for j in combinations(st,i):
        print("".join(j))
