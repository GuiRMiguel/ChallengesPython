# Desafio de Programação em Python

Este repositório contém soluções para uma série de desafios de programação em Python, baseados no curso [Desafio de Programação em Python](https://github.com/LinkedInLearning/desafio-programacao-python-3802001) do LinkedIn Learning.

Estes desafios foram projetados para testar e aprimorar suas habilidades de programação em Python. Existem diversas maneiras de resolver cada desafio, e as soluções apresentadas aqui são apenas algumas das possíveis abordagens.

## Desafios Implementados

### Desafio #1: Encontre os Fatores Primos

Implementação de uma função `fatores_primos()` que recebe um valor inteiro como argumento e retorna uma lista contendo todos os seus fatores primos.

### Desafio #2: Identifique Palíndromos

Implementação de uma função `eh_palindromo()` que verifica se um texto é um palíndromo, ignorando espaços, pontuações e diferenças de maiúsculas e minúsculas.

### Desafio #3: Ordenando Palavras em uma String

Implementação de uma função `ordenando_palavras()` que recebe uma string contendo palavras separadas por espaços e retorna uma string com essas palavras em ordem alfabética.

### Desafio #4: Encontre Todos os Itens

Implementação de uma função `encontre_indices()` que recebe uma lista de objetos e um item a ser encontrado, retornando uma lista de índices onde o item existe na lista.

### Desafio #5: Jogue o Jogo de Espera

Implementação de uma função `jogo_de_espera()` que pede ao usuário para esperar um tempo aleatório entre dois e quatro segundos antes de pressionar Enter novamente, e então verifica o tempo esperado.

### Desafio #6: Salvar Dicionário

Implementação de uma função `salvar_dicionario()` que salva um dicionário em um arquivo no formato JSON.

### Desafio #7: Agendamento de Funções

Implementação de uma função `agendar_funcao()` que agenda a execução de uma função específica em um horário determinado.

### Desafio #8: Jogue "Forca"

Implementação de um jogo da forca com a função `jogo_da_forca()` que permite ao usuário adivinhar uma palavra dentro de um número limitado de tentativas.

### Desafio #9: Simulação ao Jogar Dados

Implementação de uma função `simular_dados()` que recebe um número variável de argumentos representando dados e imprime uma tabela com a probabilidade de cada resultado possível.

### Desafio #10: Conte Palavras Únicas

Implementação de uma função `contar_palavras()` que recebe o caminho para um arquivo de texto e imprime o número total de palavras no arquivo, bem como as 20 palavras mais frequentemente usadas.

### Desafio #11: Gere uma Senha

Implementação de uma função `gerar_senha()` que gera uma senha composta por uma sequência de palavras selecionadas aleatoriamente da lista Diceware em português.

### Desafio Extra: Gere uma Senha Extremamente Complexa

Implementação de uma função `gerar_senha_complexa()` que gera uma senha altamente segura, contendo letras maiúsculas e minúsculas, números e caracteres especiais.

### Desafio #12: Unir Arquivos CSV

Implementação de uma função `unir_csv()` que recebe uma lista de nomes de arquivos CSV e um nome de arquivo de saída, unindo todos os arquivos CSV em um único arquivo.

### Desafio #13: Resolver Sudoku

Implementação de uma função `resolver_sudoku()` que recebe uma grade de Sudoku e retorna a solução do quebra-cabeça.

### Desafio #14: Compactar Arquivos em um ZIP

Implementação de uma função `compactar()` que recebe um diretório, uma lista de extensões de arquivos de interesse e um caminho para o arquivo de saída, compactando os arquivos especificados em um arquivo ZIP.

### Desafio #15: Baixar Arquivos Sequenciais

Implementação de uma função `baixar_arquivos()` que recebe a URL para a primeira imagem de uma sequência e o caminho para o diretório de destino, baixando todas as imagens sequenciais até que uma falhe.

## Como Executar

Cada desafio está implementado como uma função independente e pode ser executado individualmente. Para executar qualquer um dos desafios, basta chamar a função correspondente no bloco `if __name__ == "__main__":`.

Por exemplo, para executar o Desafio #1:

```python
if __name__ == "__main__":
    print(fatores_primos(630))  # Saída esperada: [2, 3, 3, 5, 7]
```
## Requisitos
    Python 3.x
    Bibliotecas: os, json, random, time, requests, itertools, collections, zipfile, pandas (para alguns desafios específicos)
## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias, correções de bugs ou novos desafios.

## Licença
Este projeto está licenciado sob a MIT License.

Este repositório foi criado como parte de um exercício de programação para praticar e aprimorar habilidades em Python. Cada desafio foi projetado para abordar diferentes aspectos da linguagem e de algoritmos comuns.

Referência: Desafio de Programação em Python - LinkedIn Learning