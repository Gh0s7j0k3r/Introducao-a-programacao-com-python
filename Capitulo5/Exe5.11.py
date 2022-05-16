dep_init = float(input("Informe o valor do depósito inicial: R$"))
tax_month = float(input("Informe a taxa de juros mensal: "))
count = 1
while count <= 24:
    dep_init = dep_init + (dep_init * tax_month / 100)
    print(f"{dep_init:.2f}")
    count += 1
