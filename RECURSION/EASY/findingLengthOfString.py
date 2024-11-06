from requirements import *
def Len(s,count=0):
    if s == "":
        return count
    else:
        return Len(s[1:],count+1)
    
print(Len(st))