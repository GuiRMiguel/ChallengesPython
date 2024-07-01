"""
Desafio #10: Conte palavras únicas
Seu objetivo é implementar uma função, contar_palavras(), que recebe o caminho para um arquivo de texto como argumento de entrada e imprime o número total de palavras no arquivo assim como também as 20 palavras mais frequentemente usadas e quantas vezes cada uma delas ocorre no texto.

Exemplo de entrada e saída
Usando o artigo “Notas sobre publicar meu primeiro e-book” como entrada:

>>> contar_palavras('artigo.txt')

Número total de palavras: 2395

20 palavras mais comuns:
DE      102
E       72
O       72
QUE     69
A       66
PARA    53
EM      37
LIVRO   34
UM      33
UMA     31
NO      28
DO      25
AS      22
MEU     21
COM     21
VOCÊ    21
É       20
NA      20
EU      19
COMO    19
"""

import re
from collections import Counter


def contar_palavras(caminho_arquivo):
    # Ler o conteúdo do arquivo
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        texto = file.read()

    # Processar o texto
    # Remover pontuações e converter para minúsculas
    palavras = re.findall(r'\b\w+\b', texto.lower())

    # Contar as palavras
    contador_palavras = Counter(palavras)

    # Número total de palavras
    numero_total_palavras = sum(contador_palavras.values())

    # 20 palavras mais comuns
    palavras_comuns = contador_palavras.most_common(20)

    # Exibir resultados
    print(f"Número total de palavras: {numero_total_palavras}")
    print("\n20 palavras mais comuns:")
    for palavra, contagem in palavras_comuns:
        print(f"{palavra.upper()}\t{contagem}")


if __name__ == "__main__":
    # Exemplo de uso
    contar_palavras('artigo.txt')
