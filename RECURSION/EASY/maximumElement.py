from requirements import *
def findLargestElement(arr,temp=None):
    if len(arr) == 1:
        return temp
    elif temp == None or temp < arr[1]:
        return findLargestElement(arr[1:],arr[1])
    elif temp > arr[1]:
        return findLargestElement(arr[1:],temp)
    return False

print(f"Largest element in the list:- {findLargestElement(array_list)}")