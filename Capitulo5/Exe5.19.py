valor = float(input("Digite o valor a pagar: "))
cedulas = 0
moedas = 0
atual = 100
atualm = 0.50
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R${atual}")
        if apagar < 1:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
while True:
    if atualm <= apagar:
        apagar -= atualm
        moedas += 1
    else:
        print(f"{moedas} moeda(s) de R${atualm:.2f}")
        if apagar <= 0.01:
            break
        if atualm == 0.50:
            atualm = 0.10
        elif atualm == 0.10:
            atualm = 0.05
        elif atualm == 0.05:
            atualm = 0.02
        elif atualm == 0.02:
            atualm = 0.01
        moedas = 0
