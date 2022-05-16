count = 0
ad = 0
while True:
    valor = int(input("Digite um numero a somar ou 0 para sair: "))
    if valor == 0:
        break
    count += 1
    ad += valor
print(f"Foram digitados {count} numeros, sua soma é de {ad} e sua media é {ad / count}.")
