#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
#ou 'F'. caso esteja erado, peça a digitação novamente até ter um valor correto

sexo = input("qual o seu sexo? digite [M/F] ").upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input("Digite novamente. Qual o seu sexo? digite [M/F] ").upper().strip()
print(f"Sexo igual {sexo} ")