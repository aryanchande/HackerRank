import string
def print_rangoli(size):
    al=string.ascii_lowercase
    l=[]
    for i in range(size):
        s="-".join(al[i:size])
        li=s[::-1]+s[1:]
        l.append(li)
    w=(len(l[0]))
    for i in range(size-1,0,-1):
        print(l[i].center(w,"-"))
    for i in range(size):
        print(l[i].center(w,"-"))
    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)