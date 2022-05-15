from itertools import count


x = int(input("Informe o primeiro numero da divisão: "))
y = int(input("Informe o segundo numero da divisão: "))
if x < y:
    print(f"Divisão inteira: 0\nResto da divisão: {x}")
elif x == y:
    print(f"Divisão inteira: 1\nResto da divisão: 0")
else:
    count = 0
    while x >= y:
        x -= y 
        count += 1
    print(f"Divisão inteira: {count}")
    print(f"resto da divisão: {x}")
