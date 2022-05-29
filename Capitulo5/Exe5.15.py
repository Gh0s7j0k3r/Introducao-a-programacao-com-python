total = 0
while True:
    prod = int(input("Digite o código do produto: "))
    quant = int(input("Digite a quantidade: ")) 
    if prod == 0:
        break
    if prod == 1:
        total += quant * 0.50
    elif prod == 2:
        total += quant * 1
    elif prod == 3:
        total += quant * 4
    elif prod == 5:
        total += quant * 7
    elif prod == 9:
        total += quant * 8
    else:
        print("Código invalido")
print(f"O total das compras ficou R${total:.2f}")