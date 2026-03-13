# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
st,r=input().split()
ir=int(r)
p=list(sorted(permutations(st,ir)))
for i in p:
    print("".join(map(str,i)))