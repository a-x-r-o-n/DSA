def binary(n):
    if n == 1 or n == 0:
        return f'{n}'
    else:
        return f"{binary(n//2)}" + f"{n%2}"

print(binary(16))