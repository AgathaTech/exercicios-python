"""Jogo de Adivinhação: O computador escolhe um número entre 0 e 10,
 e o jogador deve adivinhar. O jogo continua até que o jogador acerte,
 exibindo no final a quantidade de tentativas necessárias."""

import random
pc = random.randint(0,10)
palpites = 0

print("Sou o computador! Tente adivinhar o numero que estou pensando de 0 a 10 ")

while True:
    jogador = int(input('Digite seu palpite.'))
    palpites += 1

    if pc == jogador:
        print(f"Parabéns, Você acertou! Você teve {palpites} palpites ")
        break
    if jogador > pc:
        print("A dica é...Um numero abaixo desse")

    else:
        print("A dica é...Um numero acima desse ")
