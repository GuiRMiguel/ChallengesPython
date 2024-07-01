"""
Desafio #13: Solve a Sudoku
Seu objetivo é implementar uma função chamada resolver_sudoku(), que recebe como argumento de entrada uma lista bidimensional de listas representando um quebra-cabeça de Sudoku não resolvido e retorna uma lista bidimensional de listas contendo a solução do quebra-cabeça.

Atenção: Zero é usado para representar uma célula vazia.

Exemplo de entrada e saída
>>> sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
>>> resolver_sudoku(sudoku)
[[5, 3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1, 9, 8, 3, 4, 2, 5, 6, 7],
 [8, 5, 9, 7, 6, 1, 4, 2, 3],
 [4, 2, 6, 8, 5, 3, 7, 9, 1],
 [7, 1, 3, 9, 2, 4, 8, 5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]
Como um desafio extra, implemente uma função mostrar_sudoku() para exibir uma grade 9x9 de números no estilo Sudoku:

>>> mostrar_sudoku(sudoku)
 5  3  *  |  *  7  *  |  *  *  *
 6  *  *  |  1  9  5  |  *  *  *
 *  9  8  |  *  *  *  |  *  6  *
---------------------------------
 8  *  *  |  *  6  *  |  *  *  3
 4  *  *  |  8  *  3  |  *  *  1
 7  *  *  |  *  2  *  |  *  *  6
---------------------------------
 *  6  *  |  *  *  *  |  2  8  *
 *  *  *  |  4  1  9  |  *  *  5
 *  *  *  |  *  8  *  |  *  7  9
"""
import random


def mostrar_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if sudoku[i][j] == 0:
                print("*", end=" ")
            else:
                print(sudoku[i][j], end=" ")
        print()


def eh_valido(sudoku, num, pos):
    # Verificar a linha
    for i in range(len(sudoku[0])):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False

    # Verificar a coluna
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    # Verificar a caixa 3x3
    caixa_x = pos[1] // 3
    caixa_y = pos[0] // 3

    for i in range(caixa_y * 3, caixa_y * 3 + 3):
        for j in range(caixa_x * 3, caixa_x * 3 + 3):
            if sudoku[i][j] == num and (i, j) != pos:
                return False

    return True


def encontrar_vazio(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)  # linha, coluna
    return None


def resolver_sudoku(sudoku):
    encontrar = encontrar_vazio(sudoku)
    if not encontrar:
        return True
    else:
        linha, coluna = encontrar

    for i in range(1, 10):
        if eh_valido(sudoku, i, (linha, coluna)):
            sudoku[linha][coluna] = i

            if resolver_sudoku(sudoku):
                return True

            sudoku[linha][coluna] = 0

    return False


def gerar_sudoku_resolvido():
    # Cria uma grade de Sudoku vazia
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    # Preenche a grade usando a função resolver_sudoku
    resolver_sudoku(sudoku)
    return sudoku


def remover_elementos(sudoku, num_removidos=40):
    # Cria uma lista de todas as posições na grade
    posicoes = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(posicoes)

    # Remove elementos aleatórios até atingir o número desejado
    for _ in range(num_removidos):
        i, j = posicoes.pop()
        sudoku[i][j] = 0


def gerar_sudoku(num_removidos=40):
    # Gera uma grade de Sudoku resolvida
    sudoku_resolvido = gerar_sudoku_resolvido()

    # Remove elementos para criar o quebra-cabeça
    remover_elementos(sudoku_resolvido, num_removidos)

    return sudoku_resolvido


if __name__ == "__main__":
    # Gera um Sudoku a ser resolvido
    sudoku_gerado = gerar_sudoku()
    print("Sudoku gerado:")
    mostrar_sudoku(sudoku_gerado)
    print("\nResolvendo...\n")
    resolver_sudoku(sudoku_gerado)
    print("Sudoku resolvido:")
    mostrar_sudoku(sudoku_gerado)
