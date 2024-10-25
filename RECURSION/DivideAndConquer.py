def binarySearch(lst,left,right,search):
    if left > right:
        return -1
    mid = int((left+right)/2)

    if lst[mid] == search:
        return mid
    if search < lst[mid]:
        return binarySearch(lst,left,mid-1,search)
    return binarySearch(lst,mid+1,right,search)

ll = [1,2,3,4,5,6,7,8,9]
print(binarySearch(lst=ll,left=0,right=len(ll)-1,search=7))