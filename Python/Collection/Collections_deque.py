# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n=int(input())
d=deque()
for i in range(n):
    c=input().split()
    if c[0]=='append':
        d.append(c[1])
    elif c[0]=='appendleft':
        d.appendleft(c[1])
    elif c[0]=='pop':
        d.pop()
    elif c[0]=='popleft':
        d.popleft()
for i in d:
    print(i,end=' ')
