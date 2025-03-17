# 048 – faça um programa que calcule a soma entre todos os números impares que são
# múltiplos de três e que se encontram no intervalo de 1 ate 500

soma = 0 #acumulador
cont = 0 #contador
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}')