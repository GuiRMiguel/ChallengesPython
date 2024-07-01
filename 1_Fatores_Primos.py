"""
Desafio #1: Encontre os Fatores Primos
Seu objetivo é implementar uma função, fatores_primos(), que recebe um valor inteiro como argumento de entrada e retorna uma lista contendo todos os seus fatores primos.

Nota: fatores primos são todos os primos que compõem um número composto.

Exemplo de entrada e saída
fatores_primos(630)
# [2, 3, 3, 5, 7]
"""


def fatores_primos(n):
    fatores = []
    # Primeiro, lidamos com o fator 2
    while n % 2 == 0:
        fatores.append(2)
        n = n // 2

    # Depois, lidamos com os fatores ímpares a partir de 3
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            fatores.append(divisor)
            n = n // divisor
        divisor += 2

    # Se n ainda for maior que 2, ele é um fator primo
    if n > 2:
        fatores.append(n)

    return fatores

if __name__ == "__main__":
    # Teste da função com o exemplo fornecido
    print(fatores_primos(630))  # Saída esperada: [2, 3, 3, 5, 7]
