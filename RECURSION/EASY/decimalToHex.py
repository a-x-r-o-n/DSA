def hex(n):
    def getAlpha(num) -> str:
        if num == 10:
            return 'A'
        elif num == 11:
            return 'B'
        elif num == 12:
            return 'C'
        elif num == 13:
            return 'D'
        elif num == 14:
            return 'E'
        elif num == 15:
            return 'F'
        return num
    if n == 1 or n//16 == 0:
        return f'{n}'
    else:
        return f'{hex(n//16)}' + f'{getAlpha(n%16)}'
m= int(input('Number: '))
    
print(f"hex of {m}: 0x{hex(m)}\n")