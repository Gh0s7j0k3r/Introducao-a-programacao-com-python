x = int(input("Informe o primeiro numero da multiplicação: "))
y = int(input("Informe o segundo numero da multiplicação: "))
result = y
count = 1
while count < x:
    result += y
    count += 1
print(result)
