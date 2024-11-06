def triangularNumber(n):
    if n == 0:
        return n
    else:
        return triangularNumber(n-1) + n
    

print(triangularNumber(10))