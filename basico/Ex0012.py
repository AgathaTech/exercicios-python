'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
1- Abaixo de 18.5: abaixo do peso, 2- entre 18.5 e 25: peso ideal, 3- 25 até 30, sobrepeso, 4- 30 até 40: obesidade, 5- acima de 40: obesidade mórbida
'''

altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso (kg): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC: {imc:.1f} → Abaixo do peso!')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc:.1f} → Peso ideal!')
elif 25 <= imc < 30:
    print(f'IMC: {imc:.1f} → Sobrepeso!')
elif 30 <= imc < 40:
    print(f'IMC: {imc:.1f} → Obesidade!')
else:
    print(f'IMC: {imc:.1f} → Obesidade Mórbida!')