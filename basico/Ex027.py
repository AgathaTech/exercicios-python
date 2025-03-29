#crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar, [2] multiplicar, [3] maior, [4] novos numeros, [5] sair do programa
# seu programa deverá realizar a operação solicitada em cada caso

from time import sleep
n1 = int(input("Primeiro valor "))
n2 = int(input("Segundo valor "))
opção = 0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar  
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opção = int(input("Qual é sua opção? "))
    if opção == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} e {n2} é {soma} ")
    elif opção == 2:
        produto = n1 * n2
        print(f"O resultado de {n1} x {n2} é {produto} ")
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior numero entre {n1} e {n2} é {maior} ")
    elif opção == 4:
        print("Informe os numeros novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor"))
    elif opção == 5:
        print("Finalizando...")
        sleep(2)
    else:
        print("Opção inválida. Tente novamente. ")
print("Fim do programa! Volte sempre! ")

