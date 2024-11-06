from requirements import *

def minimum(arr,min=None):
    if len(arr) == 0:
        return min
    if min == None:
        min = arr[0]
    
    if min>arr[0]:
        return minimum(arr[1:],arr[0])
    else:
        return minimum(arr[1:],min)
    
print(minimum(array_list))