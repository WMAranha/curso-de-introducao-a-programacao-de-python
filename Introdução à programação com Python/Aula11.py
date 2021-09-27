lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]


except ZeroDivisionError:
    print('Não é possível realizar divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acesar um índice inválido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
