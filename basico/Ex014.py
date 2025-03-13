'''
Elabore um programa que calcule o valor a ser  pago por um produto, considerando o seu preço normal e condição de pagamento:
1- a vista dinheiro/cheque: 10% de desconto. 2- à vista no cartão: 5% de desconto, 3- em até 2x no cartão: preço normal,
4- 3x ou mais no cartão 20% de juros.
'''

produto = float(input('Valor do produto R$ '))

print('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros''')

opcao = int(input('Escolha (1, 2, 3 ou 4): '))

if opcao == 1:
    desconto = (10 / 100) * produto
    total = produto - desconto
    print(f'Total com 10% de desconto: R$ {total:.2f}')

elif opcao == 2:
    desconto = (5 / 100) * produto
    total = produto - desconto
    print(f'Total com 5% de desconto: R$ {total:.2f}')

elif opcao == 3:
    print(f'2x de R$ {produto/2:.2f} (Total: R$ {produto:.2f})')

elif opcao == 4:
    juros = (20 / 100) * produto
    total = produto + juros
    parcelas = int(input('Quantas parcelas? '))
    print(f'{parcelas}x de R$ {total/parcelas:.2f} (Total: R$ {total:.2f})')

else:
    print('Opção inválida!')