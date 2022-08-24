while True:
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4 - Multiplicação')
    print('5 - Sair')
    escolha = int(input('Informe a opção: '))
    if escolha == 5:
        break
    denominador = int(input('Informe o denominador comum para a tabuada: '))
    cont = 1
    if escolha == 1:
        while cont <= 10:
            print(f'{denominador} + {cont} = {denominador+cont}')
            cont += 1
    elif escolha == 2:
        while cont <= 10 and denominador >= cont:
            print(f'{denominador} - {cont} = {denominador-cont}')
            cont += 1
    elif escolha == 3:
        while cont <= 10:
            print(f'{denominador} / {cont} = {denominador/cont}')
            cont += 1
    elif escolha == 4:
        while cont <= 10:
            print(f'{denominador} X {cont} = {denominador*cont}')
            cont += 1
        