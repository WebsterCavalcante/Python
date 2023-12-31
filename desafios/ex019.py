# faça um programa que leia o nome de 4 alunos e sorteie 1.
import random
alu1 = input('Nome do aluno: ')
alu2 = input('Nome do aluno: ')
alu3 = input('Nome do aluno: ')
alu4 = input('Nome do aluno: ')
lista = [alu1, alu2, alu3, alu4]
print(f'\033[1mO Aluno Escolhido Foi: \033[1;35m{random.choice(lista)}')
