"""
Desafio #6: Salvar Dicionario

Escreva uma funçao que salva um dicionario em arquivo
"""

import json


def salvar_dicionario(dicionario, nome_arquivo):
    """
    Salva um dicionário em um arquivo no formato JSON.

    :param dicionario: O dicionário a ser salvo
    :param nome_arquivo: O nome do arquivo onde o dicionário será salvo
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario, arquivo, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # Exemplo de uso
    dicionario_exemplo = {
        'nome': 'Alice',
        'idade': 30,
        'cidade': 'São Paulo',
        'habilidades': ['Python', 'Machine Learning', 'Data Science']
    }
    salvar_dicionario(dicionario_exemplo, 'dicionario_exemplo.json')
    print("Dicionário salvo em 'dicionario_exemplo.json'")
