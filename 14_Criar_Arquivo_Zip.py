"""
Desafio #14: Compactar arquivos em um ZIP
Seu objetivo é implementar uma função chamada compactar(), que recebe três argumentos de entrada: o caminho para o diretório que você deseja incluir, uma lista de extensões de arquivo de interesse e um caminho para o arquivo de saída resultante.

Exemplo de entrada e saída
Usando o diretório incluído de imagens e arquivos de texto como entrada:

>>> compactar('para_compactar', ['.jpg','.txt'], 'minhas-fotos.zip')

"""

import os
import zipfile

def compactar(diretorio, extensoes, arquivo_saida):
    with zipfile.ZipFile(arquivo_saida, 'w') as zipf:
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                if any(file.endswith(ext) for ext in extensoes):
                    caminho_completo = os.path.join(root, file)
                    zipf.write(caminho_completo, os.path.relpath(caminho_completo, diretorio))
    print(f"Arquivos compactados em {arquivo_saida}")

if __name__ == "__main__":
    # Exemplo de uso
    compactar('para_compactar', ['.jpg', '.txt'], 'minhas-fotos.zip')
