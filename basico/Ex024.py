# Programa que lê nome, idade e sexo de 4 pessoas e mostra a média de idade do grupo,
# o nome do homem mais velho e quantas mulheres têm menos de 21 anos.

soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_21 = 0

for pessoa in range(4):
    print(f"DIGITE OS DADOS DA {pessoa + 1}ª PESSOA")
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (F/M): ").strip().upper()

    soma_idades += idade

    if sexo == "M":
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    elif sexo == "F" and idade < 21:
        mulheres_menos_21 += 1

media_idade = soma_idades / 4

print("===== RESULTADOS =====")
print(f"A média de idade do grupo é {media_idade:.2f} anos.")
print(f"Total de mulheres com menos de 21 anos: {mulheres_menos_21}")
if nome_homem_mais_velho:
    print(f"O homem mais velho é {nome_homem_mais_velho}, com {maior_idade_homem} anos.")
else:
    print("Nenhum homem registrado")

