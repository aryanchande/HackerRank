if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=sorted(list(set(arr)))
    ru=l[-2]
    print(ru)
