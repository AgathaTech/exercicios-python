from datetime import date
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if ano_nascimento > ano_atual:
    print("Erro: O ano de nascimento não pode ser no futuro!")
elif idade < 0:
    print("Erro: Idade inválida!")
else:
    if idade <= 9:
        categoria = "Mirim"
    elif idade <= 14:
        categoria = "Infantil"
    elif idade <= 19:
        categoria = "Junior"
    elif idade <= 20:
        categoria = "Sênior"
    else:
        categoria = "Master"

    print(f"Sua idade é {idade} e sua categoria é: {categoria}")
