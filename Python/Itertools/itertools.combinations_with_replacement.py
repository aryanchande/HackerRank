# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,n=input().split()
n=int(n)
s=sorted(s)
for j in combinations_with_replacement(s,n):
    print("".join(j))

