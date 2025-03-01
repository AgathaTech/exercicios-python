"""""Faça um programa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra 'A' em que posição ela aparece a primeira vez
em qual posição ela aparece a ultima vez"""""

frase = input("Digite uma frase ").upper().strip()
quantidade_A = frase.count('A')

if quantidade_A == 0:
    print("Não há letras A ")
else:
    primeira_posição_A = frase.find('A') + 1
    ultima_posição_A = frase.rfind('A') + 1

print(f"A frase {frase}: ")
print(f'A letra A aparece {quantidade_A} vezes ')
print(f'A letra A aparece a primeira vez em {primeira_posição_A} ')
print(f'A letra A aparece a ultima vez em {ultima_posição_A} ')