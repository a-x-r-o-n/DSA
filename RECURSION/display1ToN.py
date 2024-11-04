def display1ToN(n):
    if n == 1:
        print(1,end=' ')
        return n
    else:
        display1ToN(n-1)
        print(n,end=" ")
        
# -------------------------------
#sum from 1 to n

def sumOfNaturals(n):
    if n == 1:
        return n
    else:
        return sumOfNaturals(n-1)+n

n = int(input("Enter N'th number: "))

print(f"Sum of naturarls from 1 to {n} is {sumOfNaturals(n)}")