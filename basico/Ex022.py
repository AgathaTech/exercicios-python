#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
maioridade = 0
menoridade = 0

for ano in range(7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {ano+1} pessoa '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f'{maioridade} pessoas atingiram a maioridade e {menoridade} ainda são menores de idade.')