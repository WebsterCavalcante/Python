# faça um programa que leia um número de 0 a 9999 e mostre na tela os números separados em
# unidade, dezena, centena e milhar
print('Digite um numero entre 0 - 9999')
n = int(input('Digite um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'\033[1mUnidade: \033[1;32m{u}')
print(f'\033[m\033[1mDezena: \033[1;32m{d}')
print(f'\033[m\033[1mCentena: \033[1;32m{c}')
print(f'\033[m\033[1mMilhar: \033[1;32m{m}')
