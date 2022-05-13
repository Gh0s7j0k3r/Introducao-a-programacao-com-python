kwh = int(input("Informe a quantidade de kWh consumidos: "))
print("----------------------\nTipos de instalações\nR - Residencial\nI - Industria\nC - Comercio\n----------------------")
insta = str(input("Informe o tipo de instalação conforme quadro acima: ")).strip().upper()
if insta == "R":
    if kwh > 500:
        print(f"O valor da sua fatura ficou em R${kwh*0.65:.2f}")
    else:
        print(f"O valor da sua fatura ficou em R${kwh*0.40:.2f}")
elif insta == "I":
    if kwh > 1000:
        print(f"O valor da sua fatura ficou em R${kwh*0.60:.2f}")
    else:
        print(f"O valor da sua fatura ficou em R${kwh*0.55:.2f}")
elif insta == "C":
    if kwh > 5000:
        print(f"O valor da sua fatura ficou em R${kwh*0.60:.2f}")
    else:
        print(f"O valor da sua fatura ficou em R${kwh*0.55:.2f}")
else:
    print("Tipo de instalação invalida, por favor, realizar nova consulta!")