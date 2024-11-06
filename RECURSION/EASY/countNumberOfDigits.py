def countNumberOfDigits(n,c=0):
    if len(n) == 1:
        return c+1
    else:
        return countNumberOfDigits(n[1::],c+1)

n = input("enter Number: ")
print(countNumberOfDigits(n))