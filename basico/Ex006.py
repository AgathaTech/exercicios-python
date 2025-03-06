"""
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens
de até 200 km e R$ 0,45 para viagens mais longas.
"""

distancia = float(input('Digite a distância da viagem em km: '))

if distancia <= 200:
    valor_passagem = distancia * 0.50
else:
    valor_passagem = distancia * 0.45

print(f'Sua viagem de {distancia} km custará R$ {valor_passagem:.2f}.')