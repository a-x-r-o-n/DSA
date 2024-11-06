def factorial(n):

    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter n'th Number: "))
print(f"Factorial of 6 is {factorial(n)}")