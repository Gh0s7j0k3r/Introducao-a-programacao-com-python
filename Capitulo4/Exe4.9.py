casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o seu salário: "))
anos = int(input("Informe a quantidade de anos para pagar: "))
prest_max = float(salario * 30 / 100)
prest_aut = float(casa / (anos * 12))
if prest_max < prest_aut:
    print(f"Informamos que após analise não vai ser possivel efetuar o financiamento, o valor maximo de prestação permitido é {prest_max:.2f} e o valor da prestação para o periodo selecionado é {prest_aut:.2f}.")
    print(f"Valor da diferença: {prest_aut - prest_max:.2f}")
else:
    print(f"Financiamento autorizado, valor minimo do financiamento: R${prest_aut:.2f}\nValor autorizado da parcela para sua renda: R${prest_max:.2f}")
    