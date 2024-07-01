"""
Desafio #12: Unir arquivos CSV
Seu objetivo é implementar uma função chamada unir_csv(), que recebe dois argumentos de entrada: uma lista de nomes de arquivos CSV para unir e um nome de arquivo para salvar CSV resultante.

Exemplo de entrada e saída
Usando os dois arquivos CSV incluídos com as notas de alunos como entrada:

>>> unir_csv(['turma1.csv', 'turma2.csv'], 'alunos.csv')
"""

import pandas as pd


def unir_csv(lista_arquivos, arquivo_saida):
    # Lista para armazenar os DataFrames
    dataframes = []

    # Ler cada arquivo CSV e armazenar no DataFrame
    for arquivo in lista_arquivos:
        df = pd.read_csv(arquivo)
        dataframes.append(df)

    # Concatenar todos os DataFrames
    df_unido = pd.concat(dataframes)

    # Salvar o DataFrame unido em um novo arquivo CSV
    df_unido.to_csv(arquivo_saida, index=False)
    print(f"Arquivos unidos e salvos em {arquivo_saida}")


if __name__ == "__main__":
    # Exemplo de uso
    unir_csv(['turma1.csv', 'turma2.csv'], 'alunos.csv')
