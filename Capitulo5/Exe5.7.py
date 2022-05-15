x = int(input("Informe o valor para iniciarmos a multiplicação: "))
y = int(input("Informe o valor para finalizarmos a multiplicação: "))
if y <= x:
    print("Valor invalido, o segundo valor deve ser maior que o primeiro valor informado.")    
else:
    base = int(input("Informe o valor a ser multiplicado: "))
    while x <= y:
        print(f"{base} X {x} = {base*x}")
        x+=1