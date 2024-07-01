"""
Desafio #5: Jogue o jogo de espera
Seu objetivo é implementar uma função, jogo_de_espera(), que exibe uma mensagem para quem joga esperar por um tempo aleatório, entre dois e quatro segundos. Quando a pessoa jogando pressionar “Enter”, um cronômetro é iniciado. O objetivo de quem joga é esperar o número de segundos especificado e, em seguida, pressionar “Enter” novamente. Isso exibe o tempo decorrido, juntamente com uma mensagem informando se a pessoa jogando foi muito rápida, muito lenta ou se acertou em cheio.

Exemplo de entrada e saída
>>> jogo_de_espera()

Seu objetivo é de 2 segundos
 ---Pressione Enter para começar---

...Pressione Enter de novo depois de 2 segundos...

Tempo decorrido: 2.100 segundos
Iiii... Devagar demais... Sobrou (0.100 segundos)
"""

import time
import random


def jogo_de_espera():
    # Geração do tempo alvo entre 2 e 4 segundos
    tempo_alvo = random.uniform(2, 4)
    print(f"Seu objetivo é de {tempo_alvo:.2f} segundos")
    input("---Pressione Enter para começar---")

    print("...Pressione Enter de novo depois de {:.2f} segundos...".format(tempo_alvo))
    inicio = time.time()
    input()
    fim = time.time()

    tempo_decorrido = fim - inicio
    diferenca = tempo_decorrido - tempo_alvo

    print(f"Tempo decorrido: {tempo_decorrido:.3f} segundos")
    if abs(diferenca) < 0.1:
        print("Parabéns! Você acertou em cheio!")
    elif diferenca > 0:
        print(f"Iiii... Devagar demais... Sobrou ({diferenca:.3f} segundos)")
    else:
        print(f"Iiii... Muito rápido... Faltou ({-diferenca:.3f} segundos)")


if __name__ == "__main__":
    jogo_de_espera()
