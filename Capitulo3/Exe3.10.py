salario = float(input('Informe seu salario: '))
aumento = float(input('Informe a porcentagem do aumento: '))
aumento1 = salario*aumento/100
salario = aumento1 + salario
print('Apos o aumento de R$%.2f o salario passou a ser de R$%.2f' %(aumento1, salario))
