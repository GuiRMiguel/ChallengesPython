"""
Desafio #3: Ordenando palavras em uma string
Seu objetivo é implementar uma função chamada ordenando_palavras(), que recebe uma string contendo uma ou mais palavras separadas por espaços como argumento de entrada e retorna uma string contendo essas palavras em ordem alfabética.

Exemplo de entrada e saída
>>> ordenando_palavras('maçã LARANJA banana')
'banana LARANJA maçã'
"""


def ordenando_palavras(texto):
    # Dividir a string em palavras
    palavras = texto.split()

    # Ordenar as palavras em ordem alfabética
    palavras_ordenadas = sorted(palavras, key=lambda s: s.lower())

    # Unir as palavras ordenadas em uma string
    return ' '.join(palavras_ordenadas)

if __name__ == "__main__":
    # Testes da função com o exemplo fornecido
    print(ordenando_palavras('maçã LARANJA banana'))  # Saída esperada: 'banana LARANJA maçã'
