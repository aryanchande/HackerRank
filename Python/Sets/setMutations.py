# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int,input().split()))
m=int(input())
for i in range(m):
    l=input().split()
    if l[0]=='update':
        s=set(map(int,input().split()))
        a.update(s)
    elif l[0]=='intersection_update':
        s=set(map(int,input().split()))
        a.intersection_update(s)
    elif l[0]=='difference_update':
        s=set(map(int,input().split()))
        a.difference_update(s)
    elif l[0]=='symmetric_difference_update':
        s=set(map(int,input().split()))
        a.symmetric_difference_update(s)
print(sum(a))