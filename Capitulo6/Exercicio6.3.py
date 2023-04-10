'''Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos'''

primeira = [0,1,2,3,4]
segunda = [4,5,6,7,8,8]
terceira = primeira[:]
x=0
while x < len(segunda):
    if segunda[x] not in terceira:
        terceira.extend([segunda[x]])
    x+=1 
print(primeira)
print(segunda)
print(terceira)
