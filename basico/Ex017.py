# 047 – Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50
# Código do Professor Guanabara (Ex047 – Contagem de Pares)
# Este programa vai mostrar todos os números pares entre 1 e 50

for num in range(2, 51):
    if num % 2 == 0:
        print(num, end=' ')
