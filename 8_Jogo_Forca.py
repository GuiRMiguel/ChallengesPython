"""
Desafio #8: Jogue “forca”
Seu objetivo é implementar uma função chamada jogo_da_forca().

Essa função deverá exibir uma mensagem que exibe uma mensagem para quem joga:

Mostrando o tema escolhido
Um underline para cada letra da palavra
A quantidade de tentativas restantes
e um campo para entrada de uma letra
Além disso, a mensagem deve se manter na tela e atualizar com cada tentativa. As palavras devem ser escolhidas randomicamente de uma lista de palavras.

O objetivo de quem joga é adivinhar a palavra dentro da quantidade de tentativas disponíveis.

Tentativas incorretas diminuem a quantidade de tentativas restantes. Caso todas as tentativas acabem e a palavra não seja descoberta uma mensagem informando o fim do jogo e a palavra deve ser apresentado.

Atenção: Na solução apresentada neste repositório existem 4 temas possíveis.

Exemplo de entrada e saída
>>> jogo_da_forca()
Com o fim do jogo por exemplo...

Tema: frutas
Palavra: b a _ a _ a
Tentativas restantes: 2
Escolha uma letra: n
Acertou!
Parabéns, você adivinhou a palavra! A palavra era: banana
"""

import random


def escolher_palavra_e_tema():
    temas = {
        "frutas": ["banana", "maçã", "laranja", "uva", "abacaxi"],
        "animais": ["cachorro", "gato", "elefante", "tigre", "leão"],
        "cores": ["vermelho", "azul", "verde", "amarelo", "preto"],
        "países": ["brasil", "canada", "japão", "australia", "india"]
    }
    tema = random.choice(list(temas.keys()))
    palavra = random.choice(temas[tema])
    return tema, palavra


def jogo_da_forca():
    tema, palavra = escolher_palavra_e_tema()
    tentativas_restantes = 6
    letras_adivinhadas = []
    palavra_atual = ["_" for _ in palavra]

    print(f"Tema: {tema}")

    while tentativas_restantes > 0 and "_" in palavra_atual:
        print("\nPalavra: " + " ".join(palavra_atual))
        print(f"Tentativas restantes: {tentativas_restantes}")
        letra = input("Escolha uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já escolheu essa letra. Tente novamente.")
            continue

        letras_adivinhadas.append(letra)

        if letra in palavra:
            for idx, char in enumerate(palavra):
                if char == letra:
                    palavra_atual[idx] = letra
            print("Acertou!")
        else:
            tentativas_restantes -= 1
            print("Errou!")

    if "_" not in palavra_atual:
        print("\nParabéns, você adivinhou a palavra! A palavra era:", palavra)
    else:
        print("\nFim do jogo. Você não conseguiu adivinhar a palavra. A palavra era:", palavra)


if __name__ == "__main__":
    jogo_da_forca()
