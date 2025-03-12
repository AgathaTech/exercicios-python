'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade: 1- até 9 anos:Mirim, 2- até 14 anos: infantil, 3- até 19 anos:junior, 4- até 20 anos: sênior, 5-Acima: master'''

from datetime import date
ano_nascimento = int(input("Digite o ano de Nascimento do atleta: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if 0 <= idade <= 9:
    print(f"Sua idade é {idade} e sua categoria: Mirim ")
elif idade <= 14:
    print(f"Sua idade é {idade} e sua categoria: Infantil ")
elif idade <= 19:
    print(f"Sua idade é {idade} e sua categoria: Junior ")
elif idade <= 20:
    print(f"Sua idade é {idade} e sua categoria: Sênior ")
else:
    print(f"Sua idade é {idade} e sua categoria: Master ")