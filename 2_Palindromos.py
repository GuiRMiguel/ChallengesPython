"""
Desafio #2: Identifique Palíndromos
Seu objetivo é implementar uma função, eh_palindromo(), que recebe um texto como entrada e retorna True se o texto for um palíndromo ou False caso contrário.

Exemplo de entrada e saída
>>> eh_palindromo("Olá mundo!")
False
>>> eh_palindromo("Socorram-me, subi no ônibus em Marrocos!")
True
"""

import string


def eh_palindromo(texto):
    # Remove espaços, pontuações e transforma em minúsculas
    texto_normalizado = ''.join(char.lower() for char in texto if char.isalnum())

    # Verifica se o texto normalizado é igual à sua versão invertida
    return texto_normalizado == texto_normalizado[::-1]

if __name__ == "__main__":
    # Testes das funções com exemplos fornecidos
    print(eh_palindromo("Olá mundo!"))  # Saída esperada: False
    print(eh_palindromo("Socorram-me, subi no ônibus em Marrocos!"))  # Saída esperada: True
