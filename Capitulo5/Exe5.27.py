#Exercicio 53 do curso em video do guanabara
frase=str(input('Digite um numero: ')).strip()
palavras = frase.split()
junto=''.join(palavras)
inverso=''
#inverso=junto[::-1]
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('O inverso de {} e {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')