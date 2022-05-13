num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
print("------------------\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n------------------")
oper = int(input("Qual operação deseja fazer? "))
if oper == 1:
    print(f"Adição\n{num1} + {num2} = {num1+num2}")
elif oper == 2:
    print(f"Subtração\n{num1} - {num2} = {num1-num2}")
elif oper == 3:
    print(f"Multiplicação\n{num1} X {num2} = {num1*num2}")
elif oper == 4:
    print(f"Divisão\n{num1} / {num2} = {num1/num2:.0f}")
else:
    print("Opção invalida! Tente novamente.")
    