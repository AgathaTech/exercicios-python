#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#se o valor digitado for impar, desconsidere-o.

soma = 0
cont = 0
print('ESCREVA 6 NÚMEROS. SÓ OS PARES SERÃO SOMADOS!')

for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1  
print(f'A quantidade de números pares foi {cont} e a soma deles é {soma}')