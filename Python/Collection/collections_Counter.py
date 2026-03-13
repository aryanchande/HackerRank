# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=int(input())
s=Counter((map(int,input().split())))
n=int(input())
total=0
for _ in range(n):
    si,pr=list(map(int,input().split()))
    if s[si]>0:
        total+=pr
        s[si]-=1
print(total)


    
    
    
    
    
        
