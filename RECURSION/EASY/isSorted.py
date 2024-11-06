def isSorted(arr,n,prev):
    if len(arr) == 1 and n>=prev:
        return True
    elif prev <= n:
        return isSorted(arr[1:],arr[1],n)
    return False

l = [4,1,3,2,0,7,10,9,20]
#l.sort()
#l = [1,2,3,4,5,6,7,8,9]
print(isSorted(l,l[0],l[0]))