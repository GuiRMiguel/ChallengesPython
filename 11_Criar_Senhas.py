"""
Desafio #11: Gere uma senha
Seu objetivo é implementar uma função, gerar_senha(), que recebe como argumento a quantidade de palavras a serem incluídas na senha e retorna uma string contendo uma sequência de palavras selecionadas aleatoriamente da lista Diceware em português separadas por espaços.

Exemplo de entrada e saída
>>> gerar_senha(4)
'sanear bacilo taxar balido'


-----------------------------------------------------------------------------------------------------------------
Desafio Extra: Gere uma Senha Extremamente Complexa
Seu objetivo é implementar uma função chamada gerar_senha_complexa(), que gera uma senha extremamente complexa e segura, de acordo com os padrões de segurança modernos. A senha deve:

Ter um comprimento mínimo de 16 caracteres.
Incluir uma mistura de letras maiúsculas e minúsculas, números e caracteres especiais.
Garantir que todos os tipos de caracteres (maiúsculas, minúsculas, números e caracteres especiais) estejam presentes na senha.
Ser gerada de forma totalmente aleatória para garantir a máxima segurança.
Exemplo de entrada e saída

>>> gerar_senha_complexa()
'3f@#GzL1k9!Qw2*B'

"""

import random

# Lista Diceware em português (simplificada para o exemplo)
diceware_lista = [
    "abacate", "bacilo", "cachorro", "dado", "elefante", "faca", "gato",
    "hipopotamo", "igreja", "janela", "kilo", "lago", "macaco", "navio",
    "oceano", "pato", "quadro", "rato", "sanear", "taxar", "urso", "valente",
    "xadrez", "yamaha", "zebra", "balido", "cenoura", "diamante", "escada",
    "foguete"
]


def gerar_senha(quantidade_palavras):
    # Selecionar palavras aleatórias da lista
    palavras_selecionadas = random.sample(diceware_lista, quantidade_palavras)

    # Combinar as palavras em uma única string separada por espaços
    senha = ' '.join(palavras_selecionadas)

    return senha


import random
import string


def gerar_senha_complexa(comprimento=16):
    if comprimento < 16:
        raise ValueError("O comprimento mínimo da senha deve ser 16 caracteres.")

    # Conjuntos de caracteres
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    digitos = string.digits
    especiais = string.punctuation

    # Garantir que todos os tipos de caracteres estejam presentes
    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(digitos),
        random.choice(especiais)
    ]

    # Completar a senha até o comprimento desejado com caracteres aleatórios
    todos_caracteres = maiusculas + minusculas + digitos + especiais
    senha += random.choices(todos_caracteres, k=comprimento - len(senha))

    # Embaralhar a senha para evitar padrões previsíveis
    random.shuffle(senha)

    # Transformar a lista em string
    senha_final = ''.join(senha)

    return senha_final


if __name__ == "__main__":
    # Exemplo de uso
    print(gerar_senha(4))
    # Exemplo de uso
    print(gerar_senha_complexa())