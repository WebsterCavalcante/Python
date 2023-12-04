import random
print('escolha um dos dados abaixo')
print('A.d4 \nB.d6 \nC.d8 \nD.d10 \nE.d12 \nF.d20 \nG.d100')
escolha = str(input('Digite: ')).strip().upper()
if escolha == 'A':
    print(random.randint(1, 4))
if escolha == 'B':
    print(random.randint(1, 6))
if escolha == 'C':
    print(random.randint(1, 8))
if escolha == 'D':
    print(random.randint(1, 10))
if escolha == 'E':
    print(random.randint(1, 12))
if escolha == 'F':
    print(random.randint(1, 20))
if escolha == 'G':
    print(random.randint(1, 100))
