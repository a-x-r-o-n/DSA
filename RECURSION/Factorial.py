def countN(n):

    if n == 0:
        return 0
    
    else:
        return n + countN(n-1)

print(countN(3))