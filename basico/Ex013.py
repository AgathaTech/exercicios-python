altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso (kg): '))

if altura > 0 and peso > 0:
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
else:
    print("Erro: Altura e peso devem ser valores positivos.")

