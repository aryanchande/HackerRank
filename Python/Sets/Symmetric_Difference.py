# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
res = sorted(a.symmetric_difference(b))
for i in res:
    print(i)