def average(array):
    d=set(array)
    return sum(d)/len(d)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)