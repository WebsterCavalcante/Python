# faça um programa que leia o nome de 4 alunos e mostre a ordem sorteada.
import random
alu1 = input('nome do aluno: ')
alu2 = input('nome do aluno: ')
alu3 = input('nome do aluno: ')
alu4 = input('nome do aluno: ')
lista = [alu1, alu2, alu3, alu4]
print(f'\033[1;35m{random.sample(lista,k=4)}')
