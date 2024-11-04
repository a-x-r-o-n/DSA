def sumOfDigits(s):
    if len(s) == 1:
        return int(s)
    
    else:
        return int(s[0]) + sumOfDigits(s[1::])
    
s = input("Enter Multiple Digit Number: ")
if isinstance(int(s),int):
    print(sumOfDigits(s))
else:
    print("Enter Valid Number format")