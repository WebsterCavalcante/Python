# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor.
n = int(input('Digite um número inteiro: '))
print(f'O número digitado foi: \033[1m{n}\033[m, o sucessor de \033[1m{n} \033[mé \033[1;35m{n + 1}\033[m e o antecessor de \033[1m{n} \033[mé \033[1;35m{n - 1}')
