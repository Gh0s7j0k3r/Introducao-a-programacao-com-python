pontos = 0
questao = 1
while questao <= 3:
    resposta = str(input(f"Resposta da questão {questao}: ")).lower() #.lower() define o input como minusculo.
    if questao == 1 and resposta == "b":
        pontos += 1
    elif questao == 2 and resposta == "a":
        pontos += 1
    elif questao == 3 and resposta == "d":
        pontos += 1
    questao += 1
print(f"O aluno fez {pontos} ponto(s)")
