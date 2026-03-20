# Enter your code here. Read input from STDIN. Print output to STDOUT
e=int(input())
role=set(map(int,input().split()))
f=int(input())
rolf=set(map(int,input().split()))
s=role | rolf
print(len(s))
