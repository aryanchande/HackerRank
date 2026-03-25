# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=input().split()
rs=set(s)
for i in list(rs):
    s.remove(i)
cr=rs.difference(set(s)).pop()
print(cr)