# crie um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse angulo.
import math
angulo = eval(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno é \033[1;32m{seno:.2f}\033[m, o coseno \033[1;32m{coseno:.2f}\033[m e a tangente é \033[1;32m{tangente:.2f}')
