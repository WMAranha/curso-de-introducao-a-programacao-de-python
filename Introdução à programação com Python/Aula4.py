notatrim1 = int(input('Digite a nota do 1º trimestre:'))
while notatrim1 > 10:
    notatrim1= int(input('Você digitou errado nota do 1º. Primeiro Trimestre: '))
notatrim2 = int(input('Digite a nota do 2º trimestre:'))
while notatrim2 > 10:
    notatrim2= int(input('Você digitou errado nota do 2º. Segundo Trimestre:'))
notatrim3 = int(input('Digite a nota do 3º trimestre:'))
while notatrim3 > 10:
    notatrim3= int(input('Você digitou errado nota do 3º. Terceiro Trimestre:'))
notatrim4 = int(input('Digite a nota do 4º trimestre:'))
while notatrim4 > 10:
    notatrim4 = int(input('Você digitou errado nota do 4º. Quarto Trimestre:'))
média = (notatrim1+notatrim2+notatrim3+notatrim4)/ 4
print('Média: {}'.format(média))


# nota = int(input('Entre com a nota:'))
# while nota > 10:
#     nota = int(input('Entre com a nota correta:'))
# print(nota)

# a = int(input('Entre com um número:'))
# for num in range(a+1):
#     div=0
#     for x in range (1, num+1):
#         resto = num % x
#         #print(x,resto)
#         if resto == 0:
#             div += 1
#     if div == 2 :
#         print(num)



# a = int(input('Entre com um número:'))
# div=0
# for x in range (1, a+1):
#     resto = a % x
#     print(x,resto)
#     if resto == 0:
#         div += 1
# if div == 2 :
#     print('O número {} é primo.'.format(a))
# else:
#     print('O número {} não é primo.'.format(a))

