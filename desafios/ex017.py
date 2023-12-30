# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
cat_o = eval(input('Digite o comprimento do cateto oposto: '))
cat_a = eval(input('Digite o comprimento do cateto adjacente: '))
print(f'O cateto oposto mede: \033[1;33m{cat_o}\033[m\nO cateto adjacente mede: \033[1;33m{cat_a}\033[m\nA hipotenusa mede: \033[1;35m{hypot(cat_o,cat_a):.2f}')
