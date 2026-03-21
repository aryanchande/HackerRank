# Enter your code here. Read input from STDIN. Print output to STDOUT
en=int(input())
ren=set(map(int,input().split()))
fn=int(input())
rfn=set(map(int,input().split()))
s=ren & rfn
print(len(s))