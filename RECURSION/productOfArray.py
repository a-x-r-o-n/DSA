from requirements import *
def productOfArray(arr,val=1):
    if len(arr) == 0:
        return val
    else:
        return productOfArray(arr[1:],val*arr[0])
print(productOfArray(sorted_array))