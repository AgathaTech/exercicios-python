'''faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
1- se ele ainda vai alistar ao serviço militar, 2- se é a hora de se alistar, 3-se já passou do alistamento
Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo'''
from datetime import date
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.")
if idade == 18:
    print(f"Você deve se alistar imediatamente! ")
elif idade < 18:
    resta = 18 - idade
    ano_alistamento = ano_atual + resta
    print(f"Ainda não é hora de se alistar, falta {resta} anos ")
else:
    resta = idade - 18
    ano_alistamento = ano_atual - resta
    print(f"Você deveria ter se alistado há {resta} anos")
    print(f"Seu alistamento foi em {ano_alistamento}")


