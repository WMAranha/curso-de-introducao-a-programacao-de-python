notatrim1 = int(input('Digite a nota do 1º trimestre:'))
if notatrim1 > 10:
    notatrim1= int(input('Você digitou errado nota do 1º. Primeiro Trimestre: '))
notatrim2 = int(input('Digite a nota do 2º trimestre:'))
if notatrim2 > 10:
    notatrim2= int(input('Você digitou errado nota do 2º. Segundo Trimestre:'))
notatrim3 = int(input('Digite a nota do 3º trimestre:'))
if notatrim3 > 10:
    notatrim3= int(input('Você digitou errado nota do 3º. Terceiro Trimestre:'))
notatrim4 = int(input('Digite a nota do 4º trimestre:'))
if notatrim4 > 10:
    notatrim4 = int(input('Você digitou errado nota do 4º. Quarto Trimestre:'))
média = (notatrim1+notatrim2+notatrim3+notatrim4)/ 4
print('Média: {}'.format(média))

# if notatrim1<=10 and notatrim2<=10 and notatrim3<=10 and notatrim4<=10:
#     print('Média: {}'.format(média))
# else:
#     print('Alguma nota está errada')


# a = int(input('Primeiro valor:'))
# b = int(input ('Segundo valor:'))
# c = int(input('Terceiro valor:'))
# if a > b and a > c:
#     print('O maior número é: {}'.format(a))
# elif b > a and b > c:
#     print('O maior valor é: {}'.format(b))
# else:
#     print('O maior valor é: {}' .format(c))
# print ('Final do programa')
