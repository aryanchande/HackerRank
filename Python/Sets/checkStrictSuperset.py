# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(map(int,input().split()))
n=int(input())
ss=True
for _ in range(n):
    b=set(map(int,input().split()))
    if not a.issuperset(b):
        ss=False
print(ss)