#Desenvolva um programa que leia o primeiro termo e a razão de uma PA (PROGRESSÃO ARITMETICA).
# no final, mostre os 10 primeiros termos dessa progressão
#refaça o desafio de cima, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

primeiro = int(input("Digite o 1 termo "))
razao = int(input("Digite a razão de uma PA "))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ->', end='')
    termo = termo + razao
    cont +=1
print('fim')