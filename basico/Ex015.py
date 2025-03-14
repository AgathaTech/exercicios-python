'''Crie um programa que faça o computador jogar Jokenpô com você'''
from random import choice
lista = ["pedra","papel","tesoura"]
usuario = input("Digite entre [pedra, papel e tesoura] ").lower()
pc = choice(lista)
print(f"Usuario escolheu {usuario} e Computador escolheu {pc} ")
if pc == usuario:
    print("Empate! ")
elif usuario == 'pedra':
    if pc == 'tesoura':
        print("Você ganhou! ")
    else:
        print('Computador ganhou')
elif usuario == "tesoura":
    if pc == "papel":
        print("Você ganhou! ")
    else:
        print("Computador ganhou ")
elif usuario == "papel":
    if pc == "pedra":
        print("Você ganhou! ")
    else:
        print("Computador ganhou! ")
