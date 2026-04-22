import numpy

def arrays(arr):
    a=numpy.array(arr,dtype='f')
    return numpy.flip(a)
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)