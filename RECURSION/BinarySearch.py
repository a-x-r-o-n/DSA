BinCount = 0
LinearCount = 0
def BinarySearch(lst,left,right,x):
    global BinCount
    BinCount += 1
    if left > right:
        return -1
    mid = int((left+right)/2)
    if lst[mid] == x:
        return mid
    elif x<lst[mid]:
        return BinarySearch(lst,left,mid-1,x)
    else:
        return BinarySearch(lst,mid+1,right,x)

def LinearSearch(lst,n,y):
    global LinearCount
    LinearCount += 1
    if n == len(lst):
        return "Not Found"
    elif lst[n] == y:
        return n
    else:
        return LinearSearch(lst,n+1,y)
lst = [-1,1,2,3,4,7,9,10,20,36,38]
searchElement = 20
print(f"Binary Search\n-------------\n\n\tResult: {BinarySearch(lst=lst,left=0,right=len(lst)-1,x=searchElement)}\n\tCount: {BinCount}\n\n_____________________\n")
print(f"Linear Search\n-------------\n\n\tResult: {LinearSearch(lst=lst,n=0,y=searchElement)}\n\tCount: {LinearCount}\n")