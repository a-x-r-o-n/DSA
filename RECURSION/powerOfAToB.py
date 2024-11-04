def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return a * power(a,b-1)
a,b = int(input("enter Value for a: ")),int(input("enter Value for b: "))
print(f"{a} ^ {b} = {power(a,b)}")