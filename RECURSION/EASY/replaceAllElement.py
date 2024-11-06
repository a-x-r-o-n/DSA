from requirements import *
def replaceAll(arr=[],ele=0,replace=0,l=[]):
    if len(arr) == 0:
        return l
    elif arr[0] == ele:
        l.append(replace)
        return replaceAll(arr[1:],ele,replace,l)
    else:
        l.append(arr[0])
        return replaceAll(arr[1:],ele,replace,l)
print(replaceAll(array_list,4,111))