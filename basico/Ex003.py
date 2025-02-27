"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar. ex: US 1,00 = 5,81"""

real = float(input('Digite quanto de dinheiro você tem para converter em dólar '))
dolar = real / 5.81
print(f'Você tem R${real:.2f} e convertido em dolares você tem ${dolar:.2f} dolares ')