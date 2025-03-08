'''Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
-O primeiro valor é maior, -o segundo valor é maior, -Não existe valor maior, os dois sao iguais'''
print('\33[1;33mAbaixo, você irá digitar dois numeros sequencias para compara-los\33[m')
n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
else:
    print(f'{n1} e {n2} são numeros iguais ')