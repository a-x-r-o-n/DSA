def findOccurance(arr=[],count=0,x=0):
    if len(arr) == 0:
        return count
    elif arr[0] == x:
        return findOccurance(arr[1:],count+1,x)
    return findOccurance(arr[1:],count,x)

l = [4,1,3,2,0,7,10,9,7]
print(findOccurance(l,x=7))