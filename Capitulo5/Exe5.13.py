divida = float(input("Informe o valor inicial da divida: R$"))
juros = float(input("Informe o valor do juros mensal: "))
parcela = float(input("Informe o valor que vai ser pago mensalmente: R$"))
meses = 0
total_div = 0
atual_div = divida
while atual_div >= parcela:
    atual_div += (atual_div * juros / 100) - parcela
    meses += 1
    total_div += parcela
if atual_div < parcela:
    atual_div += (atual_div * juros / 100)
    parcela = atual_div
    atual_div -= parcela
    total_div += parcela
    meses += 1
print(f"O valor total pago foi: R${total_div:.2f}\nO valor foi quitado em {meses} meses\nO valor total de juros pago foi R${total_div-divida:.2f}")
