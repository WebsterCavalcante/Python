# a maquina vai gerar um número aleatorio e eu tenho que adivinhar
# se meu número for maior que o numero escolhido a maquina diz: o numero é menor
# se meu número for menor que o número escolhido a maquina diz: o numero é maior
import random


def adivinhe():
    maquina = random.randint(1, 3)
    print(maquina)
    numero = 0
    while numero != maquina:
        numero = int(input('Digite um número: '))
        if numero < maquina:
            print('Digite um numero maior')
        elif numero > maquina:
            print('Digite um numero menor')
        else:
            if numero == maquina:
                print('Parabens você acertou!')


adivinhe()
