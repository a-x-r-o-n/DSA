'''def count(n):

    if n == 10:
        return 10

    elif n>10:
        return "not possible"

    else:
        return n + count(n+1)

print(count(11))'''


'''def count(n):

    if n == 10:
        return 10

    else:
        return count(n-1) + n

print(count(12))'''

# The Simple Engineer

def rev(n):
    if n == "":
        return ""

    else:
        return rev(n[1:]) + n[0]


#print(rev("Aaron"))
#number system
#-------------

alphs = ['A','B','C','D','E','F']
num = 0

def dectobin(n):
    if n//2 == 0:
        return f"{n%2}"
    else:
        return  dectobin(n//2) + f"{n%2}"

#print(f"Decimal to Binary: {dectobin(num)}")

def decToOct(n):
    if n//8 == 0:
        return f"{n%8}"
    else:
        return  decToOct(n//8) + f"{n%8}"

#print(f" Decimal to OCTAL: {decToOct(num)}")

def decToHex(n):
    if n%16 == 10:
        rem = alphs[0]
    elif n%16 == 11:
        rem = alphs[1]
    elif n%16 == 12:
        rem = alphs[2]
    elif n%16 == 13:
        rem = alphs[3]
    elif n%16 == 14:

        rem = alphs[4]
    elif n%16 == 15:
        rem = alphs[5]
    else:
        rem = n%16

    if n//16 == 0:
        return f"{rem}"

    else:
        return  decToHex(n//16) + f"{rem}"

#print(f"Decimal to Hex: {decToHex(num)}")

#--------------------------------------------------------------------

def sumOfNaturalNumbers(n):
    if n <= 1:
        return n
    else:
        return n + sumOfNaturalNumbers(n-1)

print(sumOfNaturalNumbers(10))
