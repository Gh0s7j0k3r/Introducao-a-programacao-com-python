'''Escreva um programa para calcular a reducao do tempo de vida de um fumante. Perunte a quantidade de cigarros fumados por dia e quantos anos ele ja fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perdera. Exiba o total de dias.'''

cigarros = int(input('Informe a quantidade de cigarros fumados por dia: '))
anos = float(input('Informe a quantidade de anos fumando: '))
perda = anos * 365 * cigarros * 10
perdatotal = perda / (24 * 60)
print('A quantidade de dias perdidos fumando foi: %.2f' %perdatotal)
