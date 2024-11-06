from requirements import *
def evenIndex(arr,val=0,isEven=True):

    if len(arr) == 0:
        return val
    elif isEven:
        return evenIndex(arr[1:],val+arr[0],False)
    elif not isEven:
        return evenIndex(arr[1:],val,True)
print(evenIndex(sorted_array))