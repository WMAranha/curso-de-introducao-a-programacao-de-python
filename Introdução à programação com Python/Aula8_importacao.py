from Aula7_televisao import Televisao
from Aula7_calculadora1 import Calculadora
from Aula8_contador_letras import contador_letras


if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora= Calculadora(10,2)
    print(calculadora.soma())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())
    print(calculadora.subtracao())

    lista = ['cachorro','gato','elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra na lista: {}'.format(total_letras))
    