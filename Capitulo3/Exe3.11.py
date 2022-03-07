preco = float(input('Informe o valor da mercadoria: '))
desconto = float(input('Informe o valor do desconto: '))
desconto = preco*desconto/100
preco = preco - desconto
print('O desconto consedido foi de R$%.2f e o valor final ficou em R$%.2f.' %(desconto, preco))
