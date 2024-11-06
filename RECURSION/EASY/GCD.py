def gcd(a,b,i=2,g=1):
    if (a == 1 or b == 1) or (i>a or i>b):
        return g
    if a%i == 0 and b%i == 0:
        return gcd(a/i,b/i,2,g*i)
    return gcd(a,b,i+1,g)
print(gcd(int(input("Enter First Number:\t")),int(input("Enter Second Number:\t"))))