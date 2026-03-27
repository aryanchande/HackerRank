h=0
n,m=map(int,input().split())
a=input().split()
sa=set(input().split())
sb=set(input().split())
for i in a:
    if i in sa:
        h+=1
    elif i in sb:
        h-=1
print(h)