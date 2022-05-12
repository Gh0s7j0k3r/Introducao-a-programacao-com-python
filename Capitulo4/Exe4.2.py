velocidade=int(input('Informe a velocidade do veiculo: '))
val_multa=float((velocidade-80)*5)
if velocidade > 80:
    print(f'Você foi multado em R${val_multa:.2f}')