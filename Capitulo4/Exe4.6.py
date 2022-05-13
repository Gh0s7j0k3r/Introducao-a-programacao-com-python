km = int(input("Informe a distancia a percorrer: "))
if km > 200:
    valor = 0.45
else:
    valor = 0.50
print(f"O valor da passagem ficou em {km*valor}")
