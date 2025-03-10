'''Crie um programa que leia duas notas de um aluno e calcule sua média. Mostrando uma mensagem
no final, de acordo com a média atingida: 1- média abaixo de 5.0:REPROVADO, 2- MÉDIA ENTRE 5.0 E 6.9:
RECUPERAÇÃO,3- MÉDIA DE 7.0 OU SUPERIOR: APROVADO'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média do aluno foi {media:.1f}')

if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media < 7.0:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')