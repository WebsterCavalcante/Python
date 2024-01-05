# escreva um programa que pense em um número entre 0-5 e fazer o usuário descobrir o número
# o programa vai dizer se venceu ou perdeu.
from random import randint
from time import sleep
valor = randint(0, 5)
print('\033[1;33m-=-\033[m'*14)
print('\033[1;35m Mini-Game Adivinhe o Número entre 0 e 5')
print('\033[1;33m-=-\033[m'*14)
numero = int(input('Digite um número: '))
print('\033[1;34mProcessando...\033[m')
sleep(3)
if numero == valor:
    print('\033[1;32mParabens voce ganhou!\033[m')
    print(f'o número escolhido foi {valor}')
else:
    print('\033[1;31mVocê Perdeu!\033[m')
    print(f'o número escolhido foi {valor}')
