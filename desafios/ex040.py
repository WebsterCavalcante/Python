"""
Crie um program que leia 2 notas de um aluno e calcule sua media.Mostrando uma mnsagem no final,
de acordo com a media:
- de 5 : reprovado
de 5-6,9: recuperação
7 ou + :aprovado
elif r >= 7
"""
nota1: float = eval(input('Digite Sua 1ª Nota: '))
nota2: float = eval(input('Digite Sua 2ª Nota: '))
r: float = (nota1 + nota2) / 2
if r < 5:
    print(f'Média: {r}')
    print('\33[1:31mReprovado!')
elif r < 7:
    print(f'Média: {r}')
    print('\33[1:33mRecuperação.')
else:
    print(f'Média: {r}')
    print('\33[1:32mAprovado!')
