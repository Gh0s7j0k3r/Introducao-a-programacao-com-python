num1=int(input('Digite um valor: '))
num2=int(input('Digite um novo valor: '))
num3=int(input('Digite um ultimo valor: '))
maior = num1
menor = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}')
