from requirements import *
def sumOfArray(arr,val = 0):
    if len(arr) == 0:
        return val
    else:
        return sumOfArray(arr[1:],val+arr[0])
print("\n")
for i in sorted_array:
    print(i,end=' + ')
print(None,end = ' = ')
print(f"{sumOfArray(sorted_array)}")