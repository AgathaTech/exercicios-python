"""""Escreva um programa que faça o computador "pensar"
em um numero inteiro entre 0 e 5 e peça para o usuario tentar
descobrir qual foi o numero escolhido pelo computador o programa
deverá escrever na tela se o usuario venceu ou perdeu."""
import random
import time
print('==' * 20)
print('BEM VINDOS, VOU PENSAR EM UM NUMERO DE 0 A 5 E VOCE IRÁ TENTAR ADIVINHAR ')
print('==' * 20)
pc = random.randint(0,5)
usuario = int(input('Digite um numero de 0 a 5 '))
print(f' Meu numero escolhido foi........')
time.sleep(1)
print(pc)
if usuario == pc:
    print('Parabéns, você acertou! ')
else:
    print('Você errou! ')



