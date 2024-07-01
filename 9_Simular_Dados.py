"""
Desafio #9: Simulação ao jogar dados
Seu objetivo é implementar uma função chamada simular_dados(), que recebe um número variável de argumentos de entrada representando o número de lados de um número arbitrário de dados, e sua saída deve imprimir uma tabela com a probabilidade de cada resultado possível.

Exemplo de entrada e saída
Jogando um dado de quatro lados e dois dados de seis lados essas são as probabilidades:

>>> simular_dados(4,6,6)

PROBABILIDADE DE RESULTADOS
3       0.71%
4       2.08%
5       4.18%
6       6.99%
7       9.75%
8       12.49%
9       13.89%
10      13.85%
11      12.45%
12      9.71%
13      6.94%
14      4.18%
15      2.06%
16      0.70%
"""

import itertools
from collections import Counter


def simular_dados(*dados):
    # Gerar todas as combinações possíveis de resultados
    combinacoes = list(itertools.product(*(range(1, lados + 1) for lados in dados)))

    # Calcular a soma de cada combinação
    somas = [sum(combinacao) for combinacao in combinacoes]

    # Contar a frequência de cada soma
    contador = Counter(somas)

    # Calcular a probabilidade de cada soma
    total_combinacoes = len(combinacoes)
    probabilidades = {soma: (contador[soma] / total_combinacoes) * 100 for soma in contador}

    # Imprimir a tabela de probabilidades
    print("PROBABILIDADE DE RESULTADOS")
    for soma in sorted(probabilidades):
        print(f"{soma}\t{probabilidades[soma]:.2f}%")


if __name__ == "__main__":
    # Exemplo de uso
    simular_dados(4, 6, 6)
