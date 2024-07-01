"""
Desafio #15: Baixar arquivos sequenciais
Seu objetivo é implementar uma função baixar_arquivos(), que recebe dois argumentos de entrada: a URL para a primeira imagem de uma sequência e o caminho para o diretório de destino onde salvar as imagens baixadas.

Exemplo de entrada e saída
Usando o exemplo a URL a seguir que hospeda 3 imagens, sendo a primeira imagem encontrada em https://jtemporal.com/images/gitfichas/001.jpg.

>>> url = 'https://jtemporal.com/images/gitfichas/001.jpg'
>>> download_files(url, './images')
"""
import os
import requests


def baixar_arquivos(url_inicial, diretorio_destino):
    # Certifique-se de que o diretório de destino existe
    os.makedirs(diretorio_destino, exist_ok=True)

    # Extrair o prefixo da URL e o sufixo
    url_parts = url_inicial.rsplit('/', 1)
    prefixo_url = url_parts[0] + '/'
    sufixo_url = url_parts[1]

    # Determinar a parte numérica da sequência e a extensão do arquivo
    base, extensao = os.path.splitext(sufixo_url)
    num_inicial = int(base)

    while True:
        # Formar a URL para o próximo arquivo
        url = f"{prefixo_url}{str(num_inicial).zfill(len(base))}{extensao}"

        # Formar o caminho do arquivo de destino
        nome_arquivo = os.path.basename(url)
        caminho_destino = os.path.join(diretorio_destino, nome_arquivo)

        # Tentar baixar o arquivo
        response = requests.get(url)
        if response.status_code == 200:
            with open(caminho_destino, 'wb') as f:
                f.write(response.content)
            print(f"Baixado: {nome_arquivo}")
        else:
            print(f"Arquivo não encontrado: {url}")
            break

        # Incrementar o número para a próxima iteração
        num_inicial += 1


if __name__ == "__main__":
    url = 'https://jtemporal.com/images/gitfichas/001.jpg'
    baixar_arquivos(url, './images')
