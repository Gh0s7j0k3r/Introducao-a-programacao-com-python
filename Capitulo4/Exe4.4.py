salario=float(input('Informe o seu salario: '))
aumento = 15
if salario > 1250:
    aumento = 10
sal_atual= (salario * aumento / 100) + salario
print(f'Voce teve um aumento de {aumento}%, ficando com o salario de R${sal_atual:.2f}.')
