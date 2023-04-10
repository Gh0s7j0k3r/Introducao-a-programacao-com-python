'''Altere o programa da listagem 6.21 de forma a poder trabalhar com varios comandos de uma só vez. Atualmente, apenas um
comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa.'''

ultimo = 10
fila = list(range(1,ultimo + 1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S):")
    if operacao == "A":
        if(len(fila))>0:
            atendido = fila.pop(0)
            print("Cliente %d atendimento" % atendido)
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao == "F":
        ultimo+=1 #Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Dígite apenas F, A ou S!")