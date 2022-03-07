km = float(input('Informe a quantidade de KM percorrido: '))
dias = int(input('Informe a quantidade de dias com o veiculo: '))
dias = dias * 60
km = km * 0.15
total = dias + km
print('O valor total a pagar pelo aluguel do veiculo e de: R$%.2f' %total)
