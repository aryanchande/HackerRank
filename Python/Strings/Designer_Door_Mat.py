# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m=map(int,input().split())
d=".|."
w="WELCOME"

for i in range(n//2):
    p=2*i+1
    print((d*p).center(m,"-"))
print(w.center(m,"-"))
for i in range((n//2)-1,-1,-1):
    p=2*i+1
    print((d*p).center(m,"-"))
    
