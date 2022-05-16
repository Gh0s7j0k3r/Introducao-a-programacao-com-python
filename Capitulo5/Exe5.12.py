dep_init = float(input("Informe o valor do depósito mensal: R$"))
tax_month = float(input("Informe a taxa de juros mensal: "))
count = 1
mont = 0
while count <= 24:
    mont = mont + (dep_init * tax_month / 100 + dep_init)
    print(f"{mont:.2f}")
    count += 1
